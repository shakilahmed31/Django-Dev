
from django.shortcuts import render
from .forms import StudentRegistration


def Student_view(request):
  fm=StudentRegistration()
  return render(request,'enroll/student.html',{'form':fm})
