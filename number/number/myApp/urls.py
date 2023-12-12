from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('proper_divisors/<int:number>/',views.proper_divisors_view, name='proper_divisors'),
]