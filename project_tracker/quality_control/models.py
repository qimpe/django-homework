from django.db import models
from tasks.models import Project, Task
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class BugReport(models.Model):
    STATUS_CHOICES = [
        ("New", "Новая"),
        ("In_progress", "В работе"),
        ("Completed", "Завершена"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name="bug_reports",
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task, related_name="bug_reports", on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=40)
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ("Consideration", "На рассмотрении"),
        ("Accepted", "Принято"),
        ("Rejected", "Отклонено"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(
        Project, related_name="future_requests", on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task, related_name="future_requests", on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=40)
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
