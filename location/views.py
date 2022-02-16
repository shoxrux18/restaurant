
from main.models import Restaurant
from .models import Location
from .serializers import LocationSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

import haversine as hs
from haversine import Unit
from rest_framework.response import Response

# Create your views here.
import requests
import json

class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



class LocationCalculateView(APIView):
    
    def get(self, request):

        loc1=(41.3521626,69.2014573)
        lst = []
        for res in Restaurant.objects.all():
            lat, long = res.latitude, res.longitude
            aim = hs.haversine(loc1,(lat, long),unit = Unit.KILOMETERS)  
                      
            setattr(res,'distance',aim)
            lst.append(res)
        lst.sort(key=lambda x:x.distance)
        data = []
        for res in lst[:2]:
            data.append({"name": res.name_uz, "distance": f"{res.distance:0.4f}"})
        # r = requests.get(f"http://router.project-osrm.org/route/v1/car/{loc1};{lat},{long}?overview=false""")
        return Response({
            "Nearest restaurants": data
        })
          