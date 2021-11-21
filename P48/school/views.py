from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Students

class StudentsView(ListView):
  model = Students
  template_name_suffix='_gitt'
  ordering=['name']
  template_name='school/student.html'
  #def get_queryset(self):
  #  return Students.objects.filter(course='Python')
    
