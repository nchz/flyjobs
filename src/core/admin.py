from django.contrib import admin

from core.models import Job, Subscription


class SubscriptionInline(admin.TabularInline):
    model = Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscription._meta.get_fields()]
    readonly_fields = [
        "id",
        "date_created",
    ]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
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

    def save_model(self, request, obj, form, change):
        obj.publisher = request.user
        super().save_model(request, obj, form, change)
