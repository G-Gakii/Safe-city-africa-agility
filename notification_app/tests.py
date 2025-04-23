from django.test import TestCase
from django.contrib.auth import get_user_model
from report_app.models import Report
from notification_app.models import Notification

User = get_user_model()

class NotificationSignalTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com', password='pass1234'
        )

    def test_notification_on_report_creation(self):
        report = Report.objects.create(
            user=self.user,
            category_id=1,
            description="Test report description",
            severity=1,
            latitude=12.345678,
            longitude=98.765432
        )

        notification = Notification.objects.last()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.user, self.user)
        self.assertEqual(notification.notification_type, Notification.FILED_REPORT)
        self.assertIn("Thank you for your report on", notification.message)

    def test_notification_on_report_update(self):
        report = Report.objects.create(
            user=self.user,
            category_id=1,
            description="Initial description",
            severity=1,
            latitude=12.345678,
            longitude=98.765432
        )

        # Clear old notifications
        Notification.objects.all().delete()

        # Update the report to trigger update signal
        report.description = "Updated description"
        report.save()

        notification = Notification.objects.last()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.notification_type, Notification.REPORT_UPDATE)
        self.assertIn("Update on your report", notification.message)
