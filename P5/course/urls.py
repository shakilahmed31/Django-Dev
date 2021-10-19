
from django.contrib import admin
from django.urls import path
from .views import course_view

urlpatterns = [
    
    path('cv', course_view),
]
