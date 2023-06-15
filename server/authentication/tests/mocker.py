from faker import Faker
from django.contrib.auth import get_user_model

fake = Faker()
UserModel = get_user_model()


class AuthMocker:
    @staticmethod
    def generate_random_user() -> tuple:
        user = UserModel(username=fake.user_name(), email=fake.email())
        unhashed_password = fake.password()
        user.set_password(unhashed_password)
        return user, unhashed_password
