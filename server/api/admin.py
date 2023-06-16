from django.contrib import admin
from .models import Brand, Model, Car

admin.site.title_title = "Car-Api Admistration"
admin.site.site_header = "Car-Api Admistration"

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Car)
