from django.db import models
from restaurant.decorators import i18n
from django.utils.translation import gettext_lazy as _



i18n
class Restaurant(models.Model):
    STATUS_CLOSE =0
    STATUS_OPEN = 1

    STATUS_LIST = (
        (STATUS_CLOSE,_("Yopiq")),
        (STATUS_OPEN,_("Ochiq"))

    )

    name_uz = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10,decimal_places=8)
    longitude = models.DecimalField(max_digits=10,decimal_places=8)
    start_at = models.CharField(max_length=255)
    end_at = models.CharField(max_length=255)
    status = models.SmallIntegerField(choices=STATUS_LIST,default = STATUS_OPEN)
    stol = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.latitude} - {self.longitude}"



class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.RESTRICT)
    number_of_table = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    date = models.DateField(null=True)

@i18n
class OrderMenu(models.Model):
    order = models.ForeignKey(Order,on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    amount = models.IntegerField()