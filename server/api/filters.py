import django_filters
from .models import Car, Model


class CarFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    mileage = django_filters.NumberFilter()
    mileage_min = django_filters.NumberFilter(field_name="mileage", lookup_expr="gt")
    mileage_max = django_filters.NumberFilter(field_name="mileage", lookup_expr="lt")

    year_of_issue = django_filters.NumberFilter(field_name="model__year_of_issue")
    year_of_issue_min = django_filters.NumberFilter(
        field_name="model__year_of_issue", lookup_expr="gt"
    )
    year_of_issue_max = django_filters.NumberFilter(
        field_name="model__year_of_issue", lookup_expr="lt"
    )

    class Meta:
        model = Car
        fields = "__all__"


class ModelFilter(django_filters.FilterSet):
    year_of_issue = django_filters.NumberFilter()
    year_of_issue_min = django_filters.NumberFilter(
        field_name="year_of_issue", lookup_expr="gt"
    )
    year_of_issue_max = django_filters.NumberFilter(
        field_name="year_of_issue", lookup_expr="lt"
    )

    class Meta:
        model = Model
        fields = "__all__"
