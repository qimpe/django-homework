from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm
from django.views.generic.edit import UpdateView


# class views
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "quality_control/index.html")


class BugListView(ListView):
    model = BugReport
    template_name = "quality_control/bug_report_list.html"
    context_object_name = "bugs"


class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = "quality_control/bug_report_form.html"
    success_url = reverse_lazy("quality_control:bug_list")


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = "bug_id"
    template_name = "quality_control/bug_detail.html"
    context_object_name = "bug"


class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = "bug_id"
    template_name = "quality_control/bug_confirm_delete.html"
    success_url = reverse_lazy("quality_control:bug_list")
    context_object_name = "bug"


class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = "quality_control/bug_report_update.html"
    pk_url_kwarg = "bug_id"

    def get_success_url(self):
        return reverse_lazy(
            "quality_control:bug_list",
        )


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = "feature_id"
    template_name = "quality_control/feature_request_detail.html"
    context_object_name = "feature"


class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = "quality_control/feature_request_form.html"
    success_url = reverse_lazy("quality_control:feature_list")


class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = "quality_control/feature_request_list.html"
    context_object_name = "features"


class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = "quality_control/feature_update.html"
    pk_url_kwarg = "feature_id"

    def get_success_url(self):
        return reverse_lazy(
            "quality_control:feature_list",
        )


class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = "feature_id"
    template_name = "quality_control/feature_delete_confirm.html"
    success_url = reverse_lazy("quality_control:feature_list")
    context_object_name = "feature"


# function views


def index(request):
    return render(request, "quality_control/index.html")


def create_bug_report(request):
    if request.method == "POST":
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quality_control:bug_list")
    else:
        form = BugReportForm()
    return render(request, "quality_control/bug_report_form.html", {"form": form})


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, "quality_control/bug_report_list.html", {"bugs": bugs})


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, "quality_control/bug_detail.html", {"bug": bug})


def bug_update(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == "POST":
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect("quality_control:bug_detail", bug_id=bug_id)
    else:
        form = BugReportForm(instance=bug)
    return render(
        request,
        "quality_control/bug_report_update.html",
        {"form": form, "bug": bug},
    )


def bug_delete(request, bug_id):
    bug_report = get_object_or_404(BugReport, pk=bug_id)
    bug_report.delete()
    return redirect("quality_control:bug_list")


def create_feature_request(request):
    if request.method == "POST":
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quality_control:feature_list")
    else:
        form = FeatureRequestForm()
    return render(request, "quality_control/feature_request_form.html", {"form": form})


def feature_list(request):
    feature = FeatureRequest.objects.all()
    return render(
        request,
        "quality_control/feature_request_list.html",
        {"features": feature},
    )


def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(
        request, "quality_control/feature_request_detail.html", {"feature": feature}
    )


def feature_update(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == "POST":
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect("quality_control:feature_detail", feature_id=feature_id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(
        request,
        "quality_control/feature_update.html",
        {"form": form, "feature": feature},
    )


def feature_delete(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect("quality_control:feature_list")
