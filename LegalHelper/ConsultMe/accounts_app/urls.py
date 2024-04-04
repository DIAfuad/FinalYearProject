from django.contrib import admin
from django.urls import path, include
from .views import *
from accounts_app import views

urlpatterns = [
    #path('register/',views.RegisterView.as_view(), name='register'),
    path('client_register/',views.ClientSignUpView.as_view(), name='client'),
    path('lawyer_register/',views.LawyerSignUpView.as_view(), name='lawyer'),
    
    #path('client_register/',views. client_register_view, name='client'),
    
    path('choose_user/',views.choose_user_view, name='choose'),
    path('choose_login/',views.choose_login_view, name='choose_login'),
    
     
    
    path('lawyer_login/', views.LawyerLoginView.as_view(), name='lawyerlogin'),
    path('client_login/', views.ClientLoginView.as_view(), name='clientlogin'),
    
    
    
    #---------Home URL-------------
    path('lawyer_home/',views.lawyer_home_view ,name='lawyer_home'),
    path('client_home/',views.client_home_view ,name='client_home'),
    
]
