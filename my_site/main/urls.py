from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home),
   path('portfolio/', views.portfolio),
   path('contact/', views.contact),
   path('application/', views.application)
]