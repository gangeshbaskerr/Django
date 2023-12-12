# staff/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_staff, name='new_staff'),
    path('search/', views.search_staff, name='search_staff'),
    path('delete/<str:staff_id>/', views.delete_staff, name='delete_staff'),
    path('update/<str:staff_id>/', views.update_staff, name='update_staff'),
]