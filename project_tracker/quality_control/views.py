from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bug_list = reverse("quality_contol:bug_list")
    furure_request_list = reverse("quality_contol:furure_request_list")
    html = f"<h1>Система контроля качества</h1><a href='{bug_list}'>Список всех багов</a> <a href='{furure_request_list}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse("<h1>Cписок отчетов об ошибках</h1>")


def furure_request_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")


def bug_detail(request, bug_id):
    return HttpResponse(f"<h1>Детали бага {bug_id}</h1>")


def feature_id_detail(request, feature_id):
    return HttpResponse(f"<h1>Детали улучшения {feature_id}</h1>")
