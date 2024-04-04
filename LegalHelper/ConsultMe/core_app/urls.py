from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   # path('contact/',views.contact, name='contact'),
    path('contactclass/',views.Contact.as_view(), name='contact'),
]