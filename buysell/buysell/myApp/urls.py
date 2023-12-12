# vehicles/urls.py
from django.urls import path
from .views import sell_vehicle, buy_vehicle, displayvehicle

urlpatterns = [
    path('sell/', sell_vehicle, name='sell_vehicle'),
    path('buy/', buy_vehicle, name='buy_vehicle'),
    path('display/',displayvehicle)
]
