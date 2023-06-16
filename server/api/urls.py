from django.urls import path
from .views import BrandListView, ModelListView, CarListView

urlpatterns = [
    path("brands/", BrandListView.as_view(), name="brands"),
    path("models/", ModelListView.as_view(), name="models"),
    path("cars/", CarListView.as_view(), {"on_sale": True}, name="cars_on_sale"),
    path("cars/all/", CarListView.as_view(), name="cars"),
]
