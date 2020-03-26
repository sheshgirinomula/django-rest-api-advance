from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
# write your test case here


class AdminSiteTests(TestCase):
    """"""

    def setUp(self):
        """"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@londonapp.com",
            password="password123")
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@londonapp.com",
            password="password123",
            name="Test user"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        # /admin/core/user/change
        response = self.client.get(url)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.name)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/id
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        # /admin/core/user/add
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
