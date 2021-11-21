from django.contrib.auth import authenticate ,login,logout
from django.shortcuts import render ,HttpResponseRedirect,HttpResponse
from . forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



def user_login(request):
  if request.method=='POST':
    au=AuthenticationForm(request=request,data=request.POST)
    print('check:',au)
    if au.is_valid():
      uname=au.cleaned_data['username']
      upass=au.cleaned_data['password']
      user=authenticate(username=uname,password=upass)
      if user is not None:
        login(request,user)
        messages.success(request,"Suucessfully Login")
        return HttpResponseRedirect('/profile/')
          
  else:
    au=AuthenticationForm()
  return render(request,'enroll/auth.html',{'form':au})

def user_profile(request):
  return render(request,'enroll/profile.html',{'name':request.user})

def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')

def sign_up( request):
  if request.method =='POST':
    fm=SignUpForm(request.POST)
    if fm.is_valid():
      messages.success(request,"Account Created Successfully")
      fm.save()
  else:
    fm=SignUpForm()
  return render(request,'enroll/home.html',{'form':fm})

