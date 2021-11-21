from django.contrib.auth import authenticate,login ,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import Sign_Up_Form ,User_Change ,Super_User_Change
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User ,Group

def user_signup(request):
  if request.method=='POST':
    ucform=Sign_Up_Form(request.POST)
    if ucform.is_valid():
      messages.success(request,'Account Created !!!')
      user=ucform.save()
      group=Group.objects.get(name='Editor')
      user.group.add(group)
  else:
    ucform=Sign_Up_Form()
  return render(request,'school/signup.html',{'form':ucform})

def user_login(request):
  print("check1:",request)
  if request.method=='POST':
    au=AuthenticationForm(request=request,data=request.POST)
    print('Check :',au)
    if au.is_valid():
      uname=au.cleaned_data['username']
      upass=au.cleaned_data['password']
      fm=authenticate(username=uname,password=upass)
      if fm is not None:
        login(request,fm)
        return HttpResponseRedirect('/dashboard/')
  else:
    au=AuthenticationForm()
  return render(request,'school/userlogin.html',{'form':au})


def user_dashboard(request):
  if request.user.is_authenticated:
    return render (request,'school/dashboard.html',{'user':request.user.username})
  else:
   return HttpResponseRedirect('/login/')

def change_profile(request):
  if request.method=='POST':
    if request.user.is_superuser==True:
      cp=Super_User_Change(request.POST,instance=request.user)
      cp1=User.objects.all()
      
    else:
      cp=User_Change(request.POST,instance=request.user)
    if cp.is_valid():
      cp.save()
      return HttpResponseRedirect ('/login/')
  
  else:
    if request.user.is_superuser==True:
      cp=Super_User_Change(instance=request.user)
      cp1=User.objects.all()
    else:
     cp=User_Change(instance=request.user)
     cp1=None
  return render(request,'school/changeprofile.html',{'cp':cp ,'cp1':cp1}) 

def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')