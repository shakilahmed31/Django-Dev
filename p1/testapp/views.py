from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Test_func(request):
  return HttpResponse('<h1>welcome to my test visews</h1>')

def Test_func1(request):
  return HttpResponse("<h1>testing function call directly from Urls,structure is like that 'from testapp.views import Test_func1,path('Test_func1/', Test_func1),</h1>")

