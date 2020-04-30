from django.shortcuts import render
from rest_framework import generics
from .models import Trip
from .serializers import TripSerializer


class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

#class TripAvaliate(generics.RetrieveAPIView):
