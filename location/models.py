from django.db import models

# Create your models here.

class Location(models.Model):
    latitude = models.DecimalField(max_digits=10,decimal_places=8)
    longitude = models.DecimalField(max_digits=10,decimal_places=8)