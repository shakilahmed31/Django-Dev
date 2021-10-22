
from django.urls import path
from . views import Student_view

urlpatterns = [
    path('vs/',Student_view),
]
