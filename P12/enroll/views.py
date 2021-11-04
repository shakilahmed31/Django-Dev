from django.shortcuts import render
from .forms import StudentRegistration

def student_view(request):
  # if request.method=='POST':
  #   sr=StudentRegistration(request.POST)
  #   if sr.is_valid:
  #     sr.save()
  #   sr=StudentRegistration()
  # else:
  sr=StudentRegistration()
  return render(request,'enroll/home.html',{'form':sr})
