from django.db import models
from django.core.validators import MaxValueValidator

BODY_STYLES = (
    ("sedan", "Sedan"),
    ("hatchback", "HatchBack"),
    ("liftback", "Liftback"),
    ("coupe", "Coupe"),
    ("crossover", "Crossover"),
    ("truck", "Truck"),
    ("wagon", "Wagon"),
)

FUEL_TYPES = (
    ("gasoline", "Gasoline"),
    ("diesel", "Diesel"),
    ("biodiesel", "Biodiesel"),
    ("ethanol", "Ethanol"),
    ("cng", "CNG"),
    ("lpg", "LPG"),
    ("hydrogen", "Hydrogen")
)

TRANSMISSION_TYPES = (
    ("manual", "Manual"),
    ("automatic", "Automatic"),
    ("cvt", "CVT"),
    ("semi-automatic", "Semi-Automatic")
)


class Brand(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    headquarters_country = models.CharField(blank=False, null=False, max_length=56)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Model(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)
    year_of_issue = models.PositiveIntegerField(
        blank=False, null=False, validators=[MaxValueValidator(2050)]
    )
    body_style = models.CharField(
        blank=False, null=False, choices=BODY_STYLES, max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    mileage = models.PositiveIntegerField(
        blank=False, null=False, validators=[MaxValueValidator(10000000)]
    )
    exterior_color = models.CharField(blank=False, null=False, max_length=30)
    interior_color = models.CharField(blank=False, null=False, max_length=30)
    fuel_type = models.CharField(blank=False, null=False, choices=FUEL_TYPES, max_length=30)
    transmission = models.CharField(blank=False, null=False, choices=TRANSMISSION_TYPES, max_length=50)
    engine = models.CharField(blank=False, null=False, max_length=50)
    on_sale = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return f"{self.brand}: {self.model}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
