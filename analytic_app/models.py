from django.db import models
from user_app.models import User
from report_app.models import Report

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Analytic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    average_resolution_time = models.FloatField(null=True, blank=True)  # In hours
    report_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('category', 'user')  # Unique analytics per category-user pair

    def calculate_resolution_time(self):
        reports = Report.objects.filter(category=self.category, user=self.user, resolved_at__isnull=False)
        if not reports:
            return None
        total_time = sum(
            (report.resolved_at - report.created_at).total_seconds() / 3600
            for report in reports
        )
        return total_time / len(reports)

    def calculate_report_count(self):
        return Report.objects.filter(category=self.category, user=self.user).count()

    def update_analytics(self):
        self.average_resolution_time = self.calculate_resolution_time()
        self.report_count = self.calculate_report_count()
        self.save()

@receiver(post_save, sender=Report)
def update_analytics_on_report_save(sender, instance, **kwargs):
    analytics, created = Analytic.objects.get_or_create(
        category=instance.category,
        user=instance.user,
    )
    analytics.update_analytics()