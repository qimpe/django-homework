from django.urls import path
from quality_control import views

app_name = "quality_control"


# class patterns
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("bugs/", views.BugListView.as_view(), name="bug_list"),
    path("bug-detail/<int:bug_id>/", views.BugDetailView.as_view(), name="bug_detail"),
    path(
        "create-bug-report/",
        views.BugReportCreateView.as_view(),
        name="bug_create",
    ),
    path(
        "bug/<int:bug_id>/update/",
        views.BugReportUpdateView.as_view(),
        name="bug_update",
    ),
    path(
        "bug/<int:bug_id>/delete/",
        views.BugReportDeleteView.as_view(),
        name="bug_delete",
    ),
    path(
        "feature-requests/",
        views.FeatureRequestListView.as_view(),
        name="feature_list",
    ),
    path(
        "feature-detail/<int:feature_id>",
        views.FeatureRequestDetailView.as_view(),
        name="feature_detail",
    ),
    path(
        "feature-create/",
        views.FeatureRequestCreateView.as_view(),
        name="feature_create",
    ),
    path(
        "feature/<int:feature_id>/update/",
        views.FeatureRequestUpdateView.as_view(),
        name="feature_update",
    ),
    path(
        "feature/<int:feature_id>/delete/",
        views.FeatureRequestDeleteView.as_view(),
        name="feature_delete",
    ),
]


# func patterns
"""urlpatterns = [
    path("", views.index, name="index"),
    path("bugs/", views.bug_list, name="bug_list"),
    path("bug_detail/<int:bug_id>", views.bug_detail, name="bug_detail"),
    path("create-bug-report", views.create_bug_report, name="bug_create"),
    path("bug/<int:bug_id>/update/", views.bug_update, name="bug_update"),
    path("bug/<int:bug_id>/delete/", views.bug_delete, name="bug_delete"),
    path("features/", views.feature_list, name="feature_list"),
    path(
        "create-feature-request",
        views.create_feature_request,
        name="feature_create",
    ),
    path(
        "feature_detail/<int:feature_id>",
        views.feature_detail,
        name="feature_detail",
    ),
    path(
        "feature/<int:feature_id>/update", views.feature_update, name="feature_update"
    ),
    path(
        "feature/<int:feature_id>/delete", views.feature_delete, name="feature_delete"
    ),
]
"""
