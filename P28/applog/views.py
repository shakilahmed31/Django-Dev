from django.shortcuts import render ,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

def user_auth_view(request):
  if request.method=='POST':
    fm=AuthenticationForm(request=request,data=request.POST)
    if fm.is_valid():
      nm=fm.cleaned_data['username']
      pw=fm.cleaned_data['password']
      user=authenticate(username=nm,password=pw)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect('/profile/')
  
  else:
    fm=AuthenticationForm()
  return render(request,'applog/userlogin.html',{'form':fm})

