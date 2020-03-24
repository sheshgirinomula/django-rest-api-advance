from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """"""
    def test_create_user_with_email_success(self):
        """Test case creating a new user with email is successful"""
        email = "seshgiriseshgiri@gmail.com"
        user = get_user_model().objects.create_user(
            email=email, password="seshgiri")
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password("seshgiri"))
