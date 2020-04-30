from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trip/$', views.TripList.as_view(), name='trip-list'),
    url(r'^avaliate/$', views.TripAvaliate.as_view(), name='trip-avaliation'),
]