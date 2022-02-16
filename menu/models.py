from django.db import models
from main.models import Restaurant
from django.utils.translation import gettext_lazy as _
# Create your models here.




    

class Meal(models.Model):

    STATUS_AVAILABLE=1
    STATUS_UNAVAILABLE=0


    restaurant = models.ForeignKey(to=Restaurant,on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.SmallIntegerField(choices=((STATUS_AVAILABLE,_("Mavjud")),(STATUS_UNAVAILABLE,_("Mavjudmas"))))