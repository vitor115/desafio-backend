from django.shortcuts import render
from rest_framework import generics
from .models import Trip
from .serializers import TripSerializer, TripAvaliator


class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripAvaliate(generics.CreateAPIView):
    serializer_class = TripAvaliator
    
