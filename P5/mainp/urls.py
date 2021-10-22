
from django.contrib import admin
from django.urls import path
from .views import home_view ,about_view

urlpatterns = [
    path('', home_view),
    path('aboutp/',about_view,name='aboutus'), #aboutp/ is given here to check static urls limitation ,if we put about it will work
]
