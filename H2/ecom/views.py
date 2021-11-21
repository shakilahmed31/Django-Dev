from django.shortcuts import render
from django.http import HttpResponse



def index(request):
  return render(request,'ecom/index.html')

def about(request):
  return HttpResponse('We are at about')

def contact(request):
  return HttpResponse('We are at contact')

def tracker(request):
  return HttpResponse('We are at tracker')

def search(request):
  return HttpResponse('We are at about')

def productview(request):
  return HttpResponse('We are at productview page')

def checkout(request):
  return HttpResponse('We are atcheckout page ')