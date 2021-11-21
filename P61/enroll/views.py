from django.shortcuts import render
from . forms import StudentRegistration

def student(request):
  fm=StudentRegistration()
  return render(request,'enroll/home.html',{'form':fm})
