from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_sorted_edges, name='display_edges'),
]