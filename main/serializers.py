from unittest import mock
from rest_framework import serializers
from .models import Order, Restaurant
from menu.models import Meal


class RestarauntListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name_uz")


class RestaurantMenuSerializer(serializers.ModelSerializer):
    name = RestaurantSerializer(read_only = True)
    class Meta:
        model = Meal
        fields = "__all__"


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["price"]