from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Urls_making(request):
  text="<h1><i>This function is testing of direct function import to urls path for checking the import mechanism</i> </h1>"
  text2="weldone its working fine"
  return HttpResponse(text)