from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brand, Model, Car
from .serializers import BrandSerializer, ModelSerializer, CarSerializer
from .filters import CarFilter, ModelFilter


class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class ModelListView(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ModelFilter
    filterset_fields = '__all__'


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilter
    filterset_fields = '__all__'
