from django.shortcuts import render
from django.views.generic.base import TemplateView
from . models import Student
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView

class Student_View(CreateView):
  model=Student
  fields=['name','email','password']
  success_url='/done/'

class ThankYou(TemplateView):
  template_name='school/thankyou.html'

class UpdateView(UpdateView):
  model=Student
  fields=['name','email','password']
  success_url='/done/'

class StudentDeleteView(DeleteView):
  model=Student
  success_url='/create/'