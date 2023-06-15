from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker
from authentication.tests.mocker import AuthMocker

fake = Faker()


class AuthTests(APITestCase):
    def test_create_user(self):
        register_uri = reverse('user_register')
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        response = self.client.post(register_uri, {"username": username, "password": password, "confirm_password": password, "email": email})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_fail(self):
        register_uri = reverse('user_register')
        username = fake.user_name()
        password = fake.password()
        bad_password_confirm = f"{password}error"
        email = fake.email()
        response = self.client.post(register_uri, {"username": username, "password": password, "confirm_password": bad_password_confirm, "email": email})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_auth(self):
        auth_uri = reverse('token_obtain_pair')
        user, password = AuthMocker.generate_random_user()
        user.save()
        response = self.client.post(auth_uri, {"username": user.username, "password": password})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)

    def test_user_auth_fail(self):
        auth_uri = reverse('token_obtain_pair')
        user, password = AuthMocker.generate_random_user()
        bad_password = f"{password}error"
        user.save()
        response = self.client.post(auth_uri, {"username": user.username, "password": bad_password})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
