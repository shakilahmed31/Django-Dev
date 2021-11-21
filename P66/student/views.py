
from django.shortcuts import render
from datetime import datetime,timedelta

def setcookie(request):
  response= render(request,'student/setcookie.html')
  #response.set_cookie('name','sabia',max_age=60)
  #response.set_cookie('lname','sabia',expires=datetime.utcnow()+timedelta(days=2))
  response.set_signed_cookie('name','sabia',salt="nm",expires=datetime.utcnow()+timedelta(days=2))
  return response

def getcookie(request):
  nm=request.get_signed_cookie('name',default='Guest',salt='nms')
  #nm=request.COOKIES['name']
  #nm=request.COOKIES.get('name','Guest') # Guest is default value , so if user login than user name or guest
  return render(request,'student/getcookie.html',{'disp':nm})

def delcookie(request):
  response=render(request,'student/delcookie.html')
  response.delete_cookie('name')
  return response

