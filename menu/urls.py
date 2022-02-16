from django.urls import path
from .views import MealEditView,MealListView,MealCreateView
app_name='menu'

urlpatterns = [
    

    path("meal_menu/",MealListView.as_view(),name='meal_menu'),
    path("meal_create/",MealCreateView.as_view(),name='meal_create'),
    path("meal_edit/<int:pk>/",MealEditView.as_view(),name='meal_edit')
]
