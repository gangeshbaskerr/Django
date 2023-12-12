from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_ticket, name='book_ticket'),
    path('',views.show_front,name='showfront'),
    path('calculate/',views.calculate_ticket_cost,name='calculate')
]