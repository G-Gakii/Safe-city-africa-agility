from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Report(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Open")

    def resolution_time(self):
        if self.resolved_at:
            return (self.resolved_at - self.created_at).total_seconds() / 3600  # Hours
        return None

class Analytic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    average_resolution_time = models.FloatField(null=True, blank=True)  # In hours
    total_reports = models.IntegerField(default=0)
    resolved_reports = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def calculate_metrics(self):
        reports = Report.objects.filter(category=self.category)
        self.total_reports = reports.count()
        self.resolved_reports = reports.filter(status="Resolved").count()
        resolution_times = [
            report.resolution_time() for report in reports if report.resolution_time()
        ]
        self.average_resolution_time = (
            sum(resolution_times) / len(resolution_times) if resolution_times else None
        )
        self.save()

    def __str__(self):
        return f"Analytics for {self.category.name}"
