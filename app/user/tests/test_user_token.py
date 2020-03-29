from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


TOKEN_URL = reverse('user:token')


def create_user(**params):
    """"""
    return get_user_model().objects.create_user(**params)


class PublicUserTokenApiTests(TestCase):
    """Test User token creating"""

    def setUp(self):
        """"""
        self.client = APIClient()

    def test_create_token_user(self):
        """Test that token is created for the user"""
        payload = {
            'email': 'test@londonapp.com',
            'password': 'testpass',
            'name': 'test name'
        }
        create_user(**payload)
        response = self.client.post(TOKEN_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_create_token_invalid_credientials(self):
        """Test the token creation with invalid credientials"""
        create_user(email="test@londonapp.com", password="testpass")
        payload = {
            'email': 'test@londonapp.com',
            'password': 'wr'
        }
        response = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test the token not creation if user doesn't exists"""
        payload = {
            'email': 'test@londonapp.com',
            'password': 'testuser',
            'name': 'test user'
        }
        response = self.client.post(TOKEN_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn("token", response.data)

    def test_create_token_missing_field(self):
        """Test that email and password are required"""
        payload = {
            'email': 'test@londonapp.com',
            'password': ''
        }
        response = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
