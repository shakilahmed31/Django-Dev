
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Learndj_int(request):
  return HttpResponse('<h1> intermediate Django App2</h1>')

def Learnpy_int(request):
  return HttpResponse('<h1> intermediate Python App2</h1>')

