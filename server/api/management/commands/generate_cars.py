from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from api.models import Brand, Model, Car
from api.tests.mocker import APIMocker

fake = Faker()


class Command(BaseCommand):
    help: str = "Generate and save random cars"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Number of cars to generate")

    @transaction.atomic
    def handle(self, *args, **options):
        count: int = options["count"]

        for _ in range(count):
            brand: Brand = APIMocker.generate_random_brand()
            model: Model = APIMocker.generate_random_model()
            car: Car = APIMocker.generate_random_car(brand.id, model.id)
            brand.save()
            model.save()
            car.save()
