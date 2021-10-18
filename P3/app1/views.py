from django.shortcuts import render
from django.http import HttpResponse

def Learndj(request):
  return HttpResponse("<h2>Django App1 Learning Urls</h2>")

def Learnpy(request):
  return HttpResponse("<h1>Learn App1 Python urls</h1>")
