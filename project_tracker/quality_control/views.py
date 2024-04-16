from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from .models import BugReport, FeatureRequest


# class views
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "quality_control/index.html")


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = "bug_id"
    template_name = "quality_control/bug_detail.html"
    context_object_name = "bug"


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = "feature_id"
    template_name = "quality_control/feature_request_detail.html"
    context_object_name = "feature"


class BugListView(ListView):
    model = BugReport
    template_name = "quality_control/bug_report_list.html"
    context_object_name = "bugs"


class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = "quality_control/feature_request_list.html"
    context_object_name = "features"


# function views
def index(request):
    return render(request, "quality_control/index.html")


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, "quality_control/bug_report_list.html", {"bugs": bugs})


def feature_request_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(
        request,
        "quality_control/feature_request_list.html",
        {"feature_requests": feature_requests},
    )


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, "quality_control/bug_detail.html", {"bug": bug})


def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(
        request, "quality_control/feature_request_detail.html", {"feature": feature}
    )
