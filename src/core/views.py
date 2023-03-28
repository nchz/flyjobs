from rest_framework import viewsets

from core.models import JobPost
from core.serializers import JobPostSerializer


class JobPostViewSet(viewsets.ModelViewSet):
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
    # filterset_fields = ["title", "description", "location", "salary"]
    # search_fields = ["title", "description", "location"]
