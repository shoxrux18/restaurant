from django.urls import path
from .views import OrderCreateView, OrderListView, RestaurantListView,RestaurantCreateView,RestaurantEditView,RestaurantMenuView
from .views import OrderListView,OrderCreateView,OrderView
app_name='main'

urlpatterns = [
    path('restaurants/',RestaurantListView.as_view(),name='restaurants'),
    path('restaurant-create/',RestaurantCreateView.as_view(),name='restaurant-create'),
    path('restaurant-edit/<int:pk>/',RestaurantEditView.as_view(),name='restaurant-edit'),
    path('restaurant_menu/<int:pk>/',RestaurantMenuView.as_view(),name='restaurant_menu'),
    path('order_list/',OrderListView.as_view(),name='order_list'),
    path('order_create/',OrderCreateView.as_view(),name='order_create'),
    path('order/<int:tid>/',OrderView.as_view(),name='order')

]

