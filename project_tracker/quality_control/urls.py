from django.urls import path
from quality_control import views


app_name = "quality_contol"

urlpatterns = [
    path("", views.index, name="index"),
    path("bugs/", views.bug_list, name="bug_list"),
    path("futures/", views.furure_request_list, name="furure_request_list"),
    path("bug_detail/<int:bug_id>", views.bug_detail, name="bug_detail"),
    path(
        "feature_id_detail/<int:feature_id>",
        views.feature_id_detail,
        name="feature_id_detail",
    ),
]
