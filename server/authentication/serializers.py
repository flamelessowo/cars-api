from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data: dict):
        user = UserModel.objects.create(email=validated_data.get('email', ''),
                                        username=validated_data['username']
                                        )
        user.set_password(validated_data['password'])
        user.save()
        return user
