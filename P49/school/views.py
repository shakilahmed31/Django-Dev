from django.shortcuts import render
from django.views.generic.detail import DetailView
from . models import Students

class StudentDetailView(DetailView):
  model=Students

