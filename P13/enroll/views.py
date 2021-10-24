from django.shortcuts import render
from .forms import StudentRegistration ,TeacherRegistration
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
  if request.method=='POST':
    fm=UserCreationForm(request.POST)
    if fm.is_valid():
      fm.save()
  else:
    fm=UserCreationForm()
  return render(request,'enroll/signup.html',{'userf':fm})



def student_view(request):
  if request.method=='POST':
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
      sr.save()
    sr=StudentRegistration()
  else:
    sr=StudentRegistration()
  return render(request,'enroll/student.html',{'form':sr})

def teacher_view(request):
  if request.method=='POST':
    sr=TeacherRegistration(request.POST)
    if sr.is_valid():
      sr.save()
    sr=TeacherRegistration()
  else:
    sr=TeacherRegistration()
  return render(request,'enroll/teacher.html',{'form':sr})


