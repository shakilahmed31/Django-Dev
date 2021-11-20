from django.shortcuts import render
from . forms import StudentRegistration

def student_view(request):
  if request.method=='POST':
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
      n1=sr.cleaned_data['name']
      p1=sr.cleaned_data['password']
      rp1=sr.cleaned_data['rpassword']
      print('PASSWORD: ',p1,'RPASSWORD :',rp1)

  else:
    sr=StudentRegistration()
  return render(request,'paschk/index.html',{'disp':sr})


