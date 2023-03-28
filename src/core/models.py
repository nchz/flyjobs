from django.contrib.auth.models import User
from django.db import models


class JobPost(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    location = models.CharField(
        max_length=50,
        # No location may mean "remote".
        null=True,
        blank=True,
    )
    salary = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    subscriptions = models.ManyToManyField(
        User,
        # through="core.models.Subscription",
        through="Subscription",
    )


class Subscription(models.Model):
    job_post = models.ForeignKey(
        JobPost,
        on_delete=models.SET_NULL,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
