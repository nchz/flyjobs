from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import JobViewSet, UserViewSet


router = DefaultRouter()
router.register("jobs", JobViewSet, "job")
router.register("users", UserViewSet, "user")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
]
