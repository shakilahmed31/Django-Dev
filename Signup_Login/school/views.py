from django.contrib.auth import authenticate,login ,logout
from django.shortcuts import render,HttpResponseRedirect
from .forms import Sign_Up_Form ,User_Change
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm


def signup(request):
  if request.method=='POST':
    ucform=Sign_Up_Form(request.POST)
    if ucform.is_valid():
      messages.success(request,'Account Created !!!')
      ucform.save()
  else:
    ucform=Sign_Up_Form()
  return render(request,'school/index.html',{'form':ucform})

def login_view(request):
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
        return HttpResponseRedirect('/profile/')
  else:
    au=AuthenticationForm()
  return render(request,'school/userlogin.html',{'form':au})


def profile_view(request):
 
  return render(request,'school/profile.html',{'fm':request.user})

def change_pass(request):
  if request.method=='POST':
    pc=PasswordChangeForm(user=request.user,data=request.POST)
    if pc.is_valid():
      pc.save()
      return HttpResponseRedirect('/login/')
  else:
    pc=PasswordChangeForm(user=request.user)
  return render(request,'school/changepass.html',{'fm':request.user,'pc':pc})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def change_profile(request):
  if request.method=='POST':
    cp=User_Change(request.POST,instance=request.user)
    if cp.is_valid():
      cp.save()
      return HttpResponseRedirect ('/login/')
  else:
    cp=User_Change(instance=request.user)
  return render(request,'school/changeprofile.html',{'cp':cp}) 