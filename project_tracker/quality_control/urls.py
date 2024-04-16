from django.urls import path
from quality_control import views

app_name = "quality_control"

# class patterns
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("bugs/", views.BugListView.as_view(), name="bug_report_list"),
    path("bug-detail/<int:bug_id>", views.BugDetailView.as_view(), name="bug_detail"),
    path(
        "feature-requests/",
        views.FeatureRequestListView.as_view(),
        name="feature_request_list",
    ),
    path(
        "feature-detail/<int:feature_id>",
        views.FeatureRequestDetailView.as_view(),
        name="feature_detail",
    ),
]

# func patterns
"""urlpatterns = [
    path("", views.index, name="index"),
    path("bugs/", views.bug_list, name="bug_list"),
    path("futures/", views.future_request_list, name="feature_request_list"),
    path("bug_detail/<int:bug_id>", views.bug_detail, name="bug_detail"),
    path(
        "feature_detail/<int:feature_id>",
        views.feature_id_detail,
        name="feature_id_detail",
    ),
]
"""
