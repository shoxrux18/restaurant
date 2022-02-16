from django.shortcuts import render
from .serializers import MealListSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Meal
# Create your views here.



class MealListView(ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealListSerializer


class MealCreateView(CreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealListSerializer



class MealEditView(RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealListSerializer