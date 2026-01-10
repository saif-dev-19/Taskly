from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HouseSerializer
from .models import House
from .permissons import IsHouseManagerOrNone
# Create your views here.

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsHouseManagerOrNone]