from django.shortcuts import render
from . forms import StudentRegistration

def student_view(request):
  if request.method=='POST':
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
     n1=sr.cleaned_data['name']
     e1=sr.cleaned_data['email']
     p1=sr.cleaned_data['password']
     print('Name :', n1 ,'Email :', e1,'Password :', p1)

  else:
    sr=StudentRegistration()
  return render(request,'validity/index.html',{'disp':sr})
