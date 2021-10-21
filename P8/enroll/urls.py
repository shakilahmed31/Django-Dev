from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('s/',views.srudent_view),
]