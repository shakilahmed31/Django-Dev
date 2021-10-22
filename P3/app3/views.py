from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Django_fee(request):
  return HttpResponse('<h1> Django Course Fee 800 TK ,</h1>')

def Python_fee(request):
  return HttpResponse('<h1> Python Course Fee 600 TK ,</h1>')