from django.urls import path
from . import views

urlpatterns = [
    path('proper_divisors/<int:number>/', views.proper_divisors, name='proper_divisors'),
    path('classify_numbers/<int:start>/<int:end>/', views.classify_numbers, name='classify_numbers'),
]