from django.contrib import admin
from django.urls import path, include
from tasks.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", include("tasks.urls")),
    path(
        "quality-control/", include("quality_control.urls", namespace="quality_control")
    ),
]
