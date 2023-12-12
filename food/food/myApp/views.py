from django.shortcuts import render
from .models import FoodItem
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request,"home.html")
