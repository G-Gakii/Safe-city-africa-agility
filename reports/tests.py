from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Category, Report, Analytic
from django.utils import timezone
import datetime

class AnalyticTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Environmental Issues")
        self.report = Report.objects.create(
            category=self.category,
            created_at=timezone.now() - datetime.timedelta(days=1),
            resolved_at=timezone.now(),
            status="Resolved"
        )
        self.analytic = Analytic.objects.create(category=self.category)

    def test_analytic_calculation(self):
        self.analytic.calculate_metrics()
        self.assertEqual(self.analytic.total_reports, 1)
        self.assertEqual(self.analytic.resolved_reports, 1)
        self.assertAlmostEqual(self.analytic.average_resolution_time, 24.0, delta=0.1)

    def test_analytic_api(self):
        response = self.client.get(reverse('analytic-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['category']['name'], "Environmental Issues")
