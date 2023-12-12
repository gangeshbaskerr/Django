from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_grocery,name='home'),
    path('displayrecords/', views.displayrecords, name='displayrecords'),
    path('addg/', views.add_grocery,name='add'),
]