from django.urls import path
from .views import LocationCreateView,LocationCalculateView
app_name='location'

urlpatterns = [
    path("location/",LocationCreateView.as_view(),name='location'),
    path("calculate/",LocationCalculateView.as_view(),name='calculate')
]
