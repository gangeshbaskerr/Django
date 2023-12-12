# staff/views.py
from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm

def new_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_staff')
    else:
        form = StaffForm()
    return render(request, 'new_staff.html', {'form': form})

def search_staff(request):
    if request.method == 'POST':
        department = request.POST['department']
        name = request.POST['name']
        staff_list = Staff.objects.filter(department=department, name__icontains=name)
        return render(request, 'search_staff.html', {'staff_list': staff_list})
    return render(request, 'search_staff.html')

def delete_staff(request, staff_id):
    staff = Staff.objects.get(staff_id=staff_id)
    staff.delete()
    return redirect('search_staff')

def update_staff(request, staff_id):
    staff = Staff.objects.get(staff_id=staff_id)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('search_staff')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'update_staff.html', {'form': form})
