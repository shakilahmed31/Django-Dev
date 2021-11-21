from django.shortcuts import render
from django.views.generic.detail import DetailView
from . models import Students
from django.views.generic.list import ListView

class StudentDetailView(DetailView):
  model=Students
  template_name='school/student.html'
  context_object_name='stu'

class StudentList(ListView):
  model=Students
  template_name='school/students_detail.html'
  context_object_name='stu'