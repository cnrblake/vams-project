from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class SystemSecurityTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            "testadmin", "test@example.com", "testpass123"
        )

    def test_admin_panel(self):
        """Test that a logged-in admin can access the backend."""
        self.client.login(username="testadmin", password="testpass123")
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get("/admin/")
        self.assertNotEqual(response.status_code, 200)
