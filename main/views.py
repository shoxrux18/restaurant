from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Restaurant
from .serializers import OrderListSerializer, RestarauntListSerializer,RestaurantMenuSerializer,OrderCreateSerializer
from menu.models import Meal
from rest_framework.views import Response,APIView
from .models import Order
from django.db import transaction

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class =  RestarauntListSerializer


class RestaurantCreateView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class =  RestarauntListSerializer


class RestaurantEditView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class =  RestarauntListSerializer

class RestaurantMenuView(ListAPIView):
    
    def get(self, request, pk):
        return Response({
            'Restaurant_menu': RestaurantMenuSerializer(Meal.objects.filter(restaurant_id=pk),many=True).data
        })
    
    
class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

class OrderView(APIView):
    def post(self, request,tid):
        with transaction.atomic():
            table = Order.objects.get(id=tid)
            if Order.objects.filter(id=table.id).exists():
                
                return Response({
                    "data":"Bu xona bron qilingan,iltimos boshqa stol tanlang"
                })
            table.save()   

            return Response({
                "data":"Muvaffaqiyatli bron qildiniz"
            })

