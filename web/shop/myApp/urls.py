from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('studentform/', views.studentform, name='studentform'),
    path('transferToFile/', views.transferToFile, name='transferToFile'),
    path('ValidateMobile/', views.ValidateMobile, name='ValidateMobile'),
    path('input/', views.input, name='input'),
    path('table/', views.table, name='table'),
]
