from django.contrib.auth import authenticate ,login,logout
from django.shortcuts import render ,HttpResponseRedirect
from . forms import SignUpForm ,EditUserProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm 



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
  if request.user.is_authenticated:
    if request.method=='POST':
      fm=EditUserProfile(request.POST,instance=request.user)
      if fm.is_valid():
        fm.save()
    else:
      fm=EditUserProfile(instance=request.user)
    return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
  return HttpResponseRedirect('/login/')

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

def user_passchange(request):
  if request.method == 'POST':
    pc=PasswordChangeForm(user=request.user,data=request.POST)
    if pc.is_valid():
      pc.save()
      return HttpResponseRedirect('/login/')
  else:
    pc=PasswordChangeForm(user=request.user)
  print('Check PC :',pc)
  return render(request,'enroll/passchange.html',{'form':pc})

def user_profilechange(request):
  if request.method=='POST':
    fm=EditUserProfile(instance=request.user)
    if fm.is_valid():
      fm.save()
  else:
    fm=EditUserProfile()
  return render(request,'enroll/changeprofile.html',{'form':fm})