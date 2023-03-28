from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
        ]
