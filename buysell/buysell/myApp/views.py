# vehicles/views.py
from decimal import Decimal

from django.shortcuts import render, redirect
from .forms import SellForm, BuyForm
from .models import Vehicle
from django.http import HttpResponse

def sell_vehicle(request):
    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('sell_success')
    else:
        form = SellForm()
    return render(request, 'sell_vehicle.html', {'form': form})

def displayvehicle(request):
    form=Vehicle.objects.all()
    return render(request,'display.html',context={'form':form})
def buy_vehicle(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            type_of_vehicle = form.cleaned_data['type_of_vehicle']
            brand = form.cleaned_data['brand']
            kilometers = form.cleaned_data['kilometers']
            number_of_owners = form.cleaned_data['number_of_owners']
            expected_price_range = form.cleaned_data['expected_price_range']

            # Filter vehicles based on the form data
            filtered_vehicles = Vehicle.objects.filter(
                type_of_vehicle=type_of_vehicle,
                brand=brand,
                kilometers=kilometers,
            )
            if number_of_owners>0:

                filtered_vehicles = filtered_vehicles.filter(number_of_owners=number_of_owners)
            filtered_vehicles = filtered_vehicles.filter(base_price__lt=Decimal(expected_price_range))

            return render(request, 'buy_vehicle.html', {'vehicles': filtered_vehicles})
    else:
        form = BuyForm()
    return render(request, 'buy_vehicle_form.html', {'form': form})

