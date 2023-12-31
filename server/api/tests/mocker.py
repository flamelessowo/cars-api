from api.models import Brand, Model, Car, BODY_STYLES, TRANSMISSION_TYPES, FUEL_TYPES
from faker import Faker

fake = Faker()


class APIMocker:
    @staticmethod
    def generate_random_brand() -> Brand:
        return Brand.objects.create(
            name=fake.name(), headquarters_country=fake.country()
        )

    @staticmethod
    def generate_random_model() -> Model:
        return Model.objects.create(
            name=fake.name(),
            year_of_issue=fake.random_int(min=1920, max=2023),
            body_style=fake.random_element(BODY_STYLES)[0],
        )

    @staticmethod
    def generate_random_car(brand_id: str, model_id: str, sale: bool = None) -> Car:
        on_sale = fake.pybool() if sale is None else sale
        return Car.objects.create(
            brand_id=brand_id,
            model_id=model_id,
            price=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            mileage=fake.random_int(min=0, max=1000000),
            exterior_color=fake.color_name(),
            interior_color=fake.color_name(),
            fuel_type=fake.random_element(FUEL_TYPES)[0],
            transmission=fake.random_element(TRANSMISSION_TYPES)[0],
            engine=f"{fake.random_int(min=1, max=25)}L",
            on_sale=on_sale,
        )
