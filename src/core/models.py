from django.contrib.auth.models import User
from django.db import models


# TODO Define real classes.
Publisher = Candidate = User


class Job(models.Model):
    publisher = models.ForeignKey(
        Publisher,
        editable=False,
        on_delete=models.CASCADE,
        related_name="posts",
    )
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
    max_num_subs = models.PositiveIntegerField(
        default=0,
    )
    subscriptions = models.ManyToManyField(
        Candidate,
        through="Subscription",
    )

    def __str__(self):
        return f"[{self.id}] {self.title}"


class Subscription(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.SET_NULL,
        null=True,
    )
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"[{self.id}] User {self.candidate} :: Job {self.job}"
