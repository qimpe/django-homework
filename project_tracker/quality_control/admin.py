from django.contrib import admin
from .models import BugReport, FutureRequest


# Register your models here.


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "task",
        "status",
        "priority",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "priority",
        "updated_at",
    )
    search_fields = (
        "title",
        "project",
    )
    list_editable = ("status", "priority")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Title and Description", {"fields": ("title", "description")}),
        ("Task and Projects", {"fields": ("task", "project")}),
        ("Status and Priority", {"fields": ("status", "priority")}),
        ("Create/update date", {"fields": ("created_at", "updated_at")}),
    )

    def change_status(self, request, queryset):
        changed_status = queryset.update(status="Completed")
        self.message_user(
            request,
            f"Selected {changed_status} bug(s) reports was updated",
        )

    change_status.short_description = "Change status to 'Completed'"


@admin.register(FutureRequest)
class FutureRequestAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "task",
        "status",
        "priority",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "priority",
        "updated_at",
    )
    search_fields = (
        "title",
        "project",
    )
    list_editable = ("status", "priority")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Title", {"fields": ("title",)}),
        ("Task and Projects", {"fields": ("task", "project")}),
        ("Status and Priority", {"fields": ("status", "priority")}),
        ("Create/update date", {"fields": ("created_at", "updated_at")}),
    )
