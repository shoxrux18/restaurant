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
    stol = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.latitude} - {self.longitude}"



class Order(models.Model):
    order_id = models.ForeignKey(Restaurant,on_delete=models.RESTRICT)
    table = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    meal = models.ForeignKey("menu.Meal",on_delete=models.RESTRICT)
    time = models.DateTimeField(auto_now=True)

