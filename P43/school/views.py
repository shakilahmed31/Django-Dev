from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def myview(request):
  return HttpResponse('<h1> This is function Based View </h1>')

class Myview (View):
  name='Sabia'
  def get(self,request):
    #return HttpResponse('<h1> This is Class Based View-GET </h1>')
    return HttpResponse(self.name)

class MyChildview(Myview):
  def get(self,request):
    return HttpResponse (self.name)