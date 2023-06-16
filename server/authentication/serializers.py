from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ["id", "email", "username", "password", "confirm_password"]

    def create(self, validated_data: dict):
        password = validated_data["password"]

        if password != validated_data["confirm_password"]:
            raise serializers.ValidationError(
                "Password and password confirmation do not match."
            )

        user = UserModel.objects.create(
            email=validated_data.get("email", ""), username=validated_data["username"]
        )
        user.set_password(password)
        user.save()
        return user
