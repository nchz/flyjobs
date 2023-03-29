from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Job, Subscription
from core.serializers import UserSerializer, JobSerializer
from core.exceptions import AlreadySubscribedAPIException, JobFullAPIException
from core.throttling import SubscriptionRateThrottle


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    filterset_fields = ["title", "description", "location", "salary"]
    search_fields = ["title", "description", "location"]

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

    def get_permissions(self):
        if self.action in ["apply", "list", "retrieve"]:
            # Allow read-only actions and application to Candidates.
            return [permissions.IsAuthenticated()]
        else:
            return [
                # TODO Implement actual Publisher permissions.
                permissions.IsAdminUser(),
            ]

    def get_throttles(self):
        if self.action == "apply":
            return [SubscriptionRateThrottle()]
        else:
            return []

    # TODO This must use POST method since it creates resources in the db.
    @action(methods=["GET"], detail=True)
    def apply(self, request, pk=None):
        job = self.get_object()
        if job.max_num_subs != 0 and job.subscriptions.count() < job.max_num_subs:
            subs, created = Subscription.objects.get_or_create(
                job=job,
                candidate=request.user,
            )
            if created:
                return Response({"detail": "OK"})
            else:
                raise AlreadySubscribedAPIException(subs)
        else:
            raise JobFullAPIException


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Show all users to admins, only self otherwise.
        user = self.request.user
        if user.is_staff:
            return UserSerializer.Meta.model.objects.all()
        else:
            return UserSerializer.Meta.model.objects.filter(id=user.id)
