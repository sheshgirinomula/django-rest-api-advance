from django.test import  TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

PROFILE_URL = reverse('user:profile')

def create_user(**params):
    """Creates a new user"""
    return get_user_model().objects.create_user(**params)

class PrivateUserProfileApiTests(TestCase):
    """Test cases for Profile creation api that requires authentication"""

    def setUp(self):
        self.user =  create_user(
            'email' = 'test@londonapp.com',
            'password' = 'testpass',
            'name' = 'test user')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrive_profile_success(self):
        """Testing the get Profile api return status 200 Ok"""
        response = self.client.get(PROFILE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'name': self.user.name,
            'email': self.user.email
        })

    def test_post_not_allowed(self):
        """Test that post is not allowed on PROFILE_URL"""
        response = self.client.post(PROFILE_URL, {})
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_user_profile_with_correct_data(self):
        """Passing the correct payload to profile create api 
        return status 200 OK"""
        payload = {'name': 'new user', 'password': 'newspaperadd123', }
        response = self.client.patch(PROFILE_URL, payload)
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
