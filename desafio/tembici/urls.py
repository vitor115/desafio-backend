from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trips/$', views.TripList.as_view(), name='trip-list'),

]