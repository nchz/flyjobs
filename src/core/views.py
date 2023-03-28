from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Job, Subscription
from core.serializers import UserSerializer, JobSerializer
from core.exceptions import AlreadySubscribedAPIException


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

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

    # TODO This must use POST method since it creates resources in the db.
    @action(methods=["GET"], detail=True)
    def apply(self, request, pk=None):
        job = self.get_object()
        subs, created = Subscription.objects.get_or_create(
            job=job,
            candidate=request.user,
        )
        if created:
            return Response({"detail": "OK"})
        else:
            raise AlreadySubscribedAPIException(subs)


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
