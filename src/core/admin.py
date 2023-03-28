from django.contrib import admin

from core.models import JobPost, Subscription


class SubscriptionInline(admin.TabularInline):
    model = Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscription._meta.get_fields()]
    readonly_fields = [
        "id",
        "date_created",
    ]


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "date_created",
        "location",
        "salary",
    ]
    readonly_fields = [
        "id",
        "date_created",
    ]
    inlines = [
        SubscriptionInline,
    ]
