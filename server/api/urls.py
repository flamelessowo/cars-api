from django.urls import path
from .views import BrandListView, ModelListView, CarListView

urlpatterns = [
    path('brands/', BrandListView.as_view()),
    path('models/', ModelListView.as_view()),
    path('cars/', CarListView.as_view(), {'on_sale': True}),
    path('cars/all/', CarListView.as_view()),
]
