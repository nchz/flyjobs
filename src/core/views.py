from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Job, Subscription
from core.serializers import UserSerializer, JobSerializer
from core.exceptions import AlreadySubscribedAPIException


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    # filterset_fields = ["title", "description", "location", "salary"]
    # search_fields = ["title", "description", "location"]

    # TODO This must use POST method since it creates resources in the db.
    @action(methods=["GET"], detail=True)
    def apply(self, request, pk=None):
        job = self.get_object()
        subs, created = Subscription.objects.get_or_create(
            job=job,
            user=request.user,
        )
        if created:
            return Response({"detail": "OK"})
        else:
            raise AlreadySubscribedAPIException(subs)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
