from django.contrib.auth import authenticate ,login,logout
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm ,PasswordChangeForm ,SetPasswordForm,UserChangeForm
from django.contrib import messages
from django.http import HttpResponseRedirect

#SignUp
def sign_up(request):
  if request.method=="POST":
    fm=UserCreationForm(request.POST)
    if fm.is_valid():
      messages.success(request,"Account Successfully Created !!")
      fm.save()
    fm=UserCreationForm()
  else:
    fm= UserCreationForm()
  return render(request,'enroll/home.html',{'form':fm})

#login

def user_login(request):
  if request.method=='POST':
    fm=AuthenticationForm(request=request,data=request.POST)
    if fm.is_valid():
      un=fm.cleaned_data['username']
      pw=fm.cleaned_data['password']
      user=authenticate(username=un,password=pw)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect('/profile/')
  else:
    fm=AuthenticationForm()
  return render(request,'enroll/userlogin.html',{'form':fm})

def thankyou(request):
  return render(request,'enroll/thankyou.html',{'name':request.user})

def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')

def user_changepass(request):
  if request.method=='POST':
    fm=PasswordChangeForm(user=request.user,data=request.POST)
    if fm.is_valid():
      fm.save()
      return HttpResponseRedirect('/login/')
  else:
    fm=PasswordChangeForm(user=request.user)
  return render(request,'enroll/changepass.html',{'form':fm})  

def user_changepass1(request):
  if request.method=='POST':
    fm=SetPasswordForm(user=request.user,data=request.POST)
    if fm.is_valid():
      fm.save()
      return HttpResponseRedirect('/login/')
  else:
    fm=SetPasswordForm(user=request.user)
  return render(request,'enroll/changepass1.html',{'form':fm})  

def user_profile(request):
  if request.user.is_authenticated:
    fm=UserChangeForm(instance=request.user)
    return render(request,'enroll/profile.html',{'name':request.user,'form':fm}) 
  else:
    return HttpResponseRedirect('/profile/')


