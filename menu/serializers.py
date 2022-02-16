from rest_framework import serializers
from .models import Meal





class MealListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = ("__all__")

class MealListEditSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Meal
        fields = ("__all__")