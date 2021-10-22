
from django.contrib import admin
from django.urls import path
from passchk import views

urlpatterns = [
    path('s/', views.showdata),
]