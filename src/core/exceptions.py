from rest_framework import status
from rest_framework.exceptions import APIException


class AlreadySubscribedAPIException(APIException):
    status_code = status.HTTP_409_CONFLICT

    def __init__(self, subs, *args, **kwargs):
        detail = f"User already subscribed with date {subs.date_created}"
        super().__init__(detail=detail, *args, **kwargs)


class JobFullAPIException(APIException):
    default_detail = "Job has reached limit of subscriptions."
    status_code = status.HTTP_409_CONFLICT
