
from django.shortcuts import render ,HttpResponseRedirect
from . forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm ,UserChangeForm
from django.contrib.auth import authenticate,login,logout

def sign_up(request):
  if request.method=="POST":
    fm=SignUpForm(request.POST)
    if fm.is_valid():
      fm.save()

    fm=SignUpForm()
  else:
    fm=SignUpForm()
  return render(request,'enroll/signup.html',{'form':fm})

def user_login(request):
  if request.method=="POST":
    fm=AuthenticationForm(request=request ,data=request.POST)
    print (fm)
    if fm.is_valid():
      uname=fm.cleaned_data['username']
      upass=fm.cleaned_data['password']
      user=authenticate(username=uname ,password=upass)
      print(user)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect('/profile/')
  else:
    fm=AuthenticationForm() 
  return render(request,'enroll/userlogin.html',{'form':fm})


def user_profile(request):
  if request.user.is_autheticated:
    fm=UserChangeForm(instance=request.user)
    
    return render(request,'enroll/profile.html',{'name':request.user , 'form':fm})

  else:
    return HttpResponseRedirect('/login/')

def user_logout(request):
  logout(request)
  return HttpResponseRedirect('/login/')

def user_pass_change(request):
  if request.method =='POST':
    fm=PasswordChangeForm(user=request.user,data= request.POST)
    if fm.is_valid():
      fm.save()
      return HttpResponseRedirect('/profile/')
  else:
    fm=PasswordChangeForm(user=request.user)
  return render(request,'enroll/changepass.html',{'form':fm})