from django.shortcuts import render
from . forms import StudentRegistration
from .models import User

def showdata(request):
  if request.method=='POST':
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
      nm=sr.cleaned_data['name']
      em=sr.cleaned_data['email']
      pm=sr.cleaned_data['password']
      reg=User(name=nm,email=em,password=pm)
      reg.save()
     
  else:
    sr=StudentRegistration()

  return render(request,'enroll/index.html',{'form':sr})