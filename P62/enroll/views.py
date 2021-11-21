from django.shortcuts import render
from . forms import StudentRegistration

def student(request):
  if request.method=='POST':
    fm=StudentRegistration(request.POST)
    if fm.is_valid():
      print(fm)
  else:
    fm=StudentRegistration()
  return render(request,'enroll/home.html',{'form':fm})
