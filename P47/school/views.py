from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Students

class StudentsView(ListView):
  model = Students


