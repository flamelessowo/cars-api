from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker
from api.tests.mocker import APIMocker
from authentication.tests.mocker import AuthMocker

fake = Faker()


class APITests(APITestCase):
    def setUp(self):
        self.token = self.get_auth_token()
        self.auth_header = {"Authorization": f"Bearer {self.token}"}

    def get_auth_token(self) -> str:
        user, password = AuthMocker.generate_random_user()
        user.save()
        auth_uri = reverse("token_obtain_pair")
        response = self.client.post(
            auth_uri, {"username": user.username, "password": password}
        )
        return response.data["access"]

    def test_get_brands(self):
        BRANDS_TO_GENERATE = 20
        brands_uri = reverse("brands")
        for _ in range(BRANDS_TO_GENERATE):
            brand = APIMocker.generate_random_brand()
            brand.save()
        response = self.client.get(brands_uri, headers=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), BRANDS_TO_GENERATE)

    def test_get_brands_fail(self):
        brands_uri = reverse("brands")
        response = self.client.get(brands_uri)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_models(self):
        MODELS_TO_GENERATE = 20
        models_uri = reverse("models")
        for _ in range(MODELS_TO_GENERATE):
            model = APIMocker.generate_random_model()
            model.save()
        response = self.client.get(models_uri, headers=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), MODELS_TO_GENERATE)

    def test_get_models_fail(self):
        models_uri = reverse("models")
        response = self.client.get(models_uri)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_cars(self):
        CARS_TO_GENERATE = 20
        cars_sale_uri = reverse("cars_on_sale")
        for _ in range(CARS_TO_GENERATE):
            brand = APIMocker.generate_random_brand()
            model = APIMocker.generate_random_model()
            car = APIMocker.generate_random_car(brand.id, model.id, sale=True)
            brand.save()
            model.save()
            car.save()
        response = self.client.get(cars_sale_uri, headers=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), CARS_TO_GENERATE)
        self.assertTrue(all(car["on_sale"] for car in response.data))

    def test_get_cars_fail(self):
        cars_sale_uri = reverse("cars_on_sale")
        response = self.client.get(cars_sale_uri)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_cars_all(self):
        CARS_TO_GENERATE = 20
        cars_uri = reverse("cars")
        for _ in range(CARS_TO_GENERATE):
            brand = APIMocker.generate_random_brand()
            model = APIMocker.generate_random_model()
            car = APIMocker.generate_random_car(brand.id, model.id)
            brand.save()
            model.save()
            car.save()
        response = self.client.get(cars_uri, headers=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), CARS_TO_GENERATE)

    def test_get_cars_all_fail(self):
        cars_uri = reverse("cars")
        response = self.client.get(cars_uri)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
