from django.db import models

BODY_STYLES = (
    ('sedan', 'Sedan'),
    ('hatchback', 'HatchBack'),
    ('liftback', 'Liftback'),
    ('coupe', 'Coupe'),
    ('crossover', 'Crossover'),
    ('truck', 'Truck'),
    ('wagon', 'Wagon')
)


class Brand(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=100)
    headquarters_country = models.CharField(blank=False, null=False, max_length=56)


class Model(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(blank=False, null=False, max_length=100)
    year_of_issue = models.DateField(null=False, blank=False)
    body_style = models.CharField(blank=False, null=False, choices=BODY_STYLES, max_length=100)


class Car(models.Model):
    id = models.UUIDField(primary_key=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    mileage = models.PositiveIntegerField()
    exterior_color = models.CharField(blank=False, null=False, max_length=30)
    interior_color = models.CharField(blank=False, null=False, max_length=30)
    fuel_type = models.CharField(blank=False, null=False, max_length=30)
    transmission = models.CharField(blank=False, null=False, max_length=50)
    engine = models.CharField(blank=False, null=False, max_length=50)
    on_sale = models.BooleanField(blank=False, null=False, default=False)
