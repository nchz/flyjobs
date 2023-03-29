"""
The fixture for these tests contain 2 Users: "root:asd" that is admin, and
"foo:bar". It also contains 2 Jobs: the Job with id=2 contains 1 subscription,
from user "root".
"""

from rest_framework.test import APITestCase

from core.models import Job


class TestURLConfig(APITestCase):
    def test_redirect(self):
        res = self.client.get("/api")
        self.assertEqual(res.status_code, 301)


class TestListPlayers(APITestCase):
    fixtures = ["test-data.json"]

    def test_create_job_not_allowed_for_regular_user(self):
        self.client.login(username="foo", password="bar")
        res = self.client.post(
            "/api/jobs/",
            data={
                "title": "test",
                "description": "desc",
            },
        )
        self.assertEqual(res.status_code, 403)

    def test_already_subscribed(self):
        self.client.login(username="root", password="asd")
        res = self.client.get("/api/jobs/2/apply/")
        self.assertEqual(res.status_code, 409)

    def test_create_job_and_subscribe(self):
        self.client.login(username="root", password="asd")
        # Create a Job.
        res = self.client.post(
            "/api/jobs/",
            data={
                "title": "test",
                "description": "desc",
            },
        )
        # Subscribe to it.
        res = self.client.get(f"{res.data['url']}apply/")
        num_subscriptions = Job.objects.get(title="test").subscriptions.count()
        self.assertEqual(num_subscriptions, 1)
