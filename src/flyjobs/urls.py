from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from core.views import JobViewSet, UserViewSet


router = DefaultRouter()
router.register("jobs", JobViewSet, "job")
router.register("users", UserViewSet, "user")

schema_view = get_schema_view(
    title="Flyjobs",
    description="API details.",
)

swagger_view = TemplateView.as_view(
    template_name="swagger-ui.html",
    extra_context={"schema_url": "openapi-schema"},
)


urlpatterns = [
    path("", swagger_view, name="swagger-ui"),
    path("schema/", schema_view, name="openapi-schema"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
]
