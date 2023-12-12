from django.shortcuts import render, redirect
from .models import Grocery
from .forms import GroceryForm

def displayrecords(request):
    groceries = Grocery.objects.all().values()
    return render(request,'display_records.html',{'groceries':groceries})

def add_grocery(request):
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            grocery = form.save(commit=False)
            grocery.amount = grocery.quantity * grocery.rate_per_unit
            grocery.save()
            return redirect('displayrecords')
    else:
        form = GroceryForm()
    return render(request, 'add_grocery.html',{'form':form})