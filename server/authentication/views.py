from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, decorators, status
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

UserModel = get_user_model()


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
