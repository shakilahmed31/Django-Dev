
from django.urls import path
from . views import showdata

urlpatterns = [
    path('regi/',showdata),
]