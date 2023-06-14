from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from faker import Faker
from api.models import Brand, Model, Car, BODY_STYLES

fake = Faker()


def generateRandomBrand() -> Brand:
    return Brand.objects.create(name=fake.name(), headquarters_country=fake.country())


def generateRandomModel() -> Model:
    return Model.objects.create(name=fake.name(), year_of_issue=fake.random_int(min=1920, max=2023), body_style=fake.random_element(BODY_STYLES)[0])


def generateRandomCar(brand_id: str, model_id: str) -> Car:
    return Car.objects.create(brand_id=brand_id, model_id=model_id, price=fake.pydecimal(left_digits=5, right_digits=2, positive=True), mileage=fake.random_int(min=0, max=1000000), exterior_color=fake.color_name(), interior_color=fake.color_name(), fuel_type=fake.name(), transmission=fake.name(), engine=f'{fake.random_int(min=1, max=25)}L', on_sale=fake.pybool())


class Command(BaseCommand):
    help: str = 'Generate and save random cars'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of cars to generate')

    @transaction.atomic
    def handle(self, *args, **options):
        count: int = options['count']

        for _ in range(count):
            brand: Brand = generateRandomBrand()
            model: Model = generateRandomModel()
            car: Car = generateRandomCar(brand.id, model.id)
            brand.save()
            model.save()
            car.save()
