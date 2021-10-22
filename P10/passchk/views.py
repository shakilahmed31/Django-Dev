from django.shortcuts import render
from passchk.forms import StudentRegistration


def showdata(request):
  if request.method=='POST':
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
      print('Form Validated')
      print('Name',sr.cleaned_data['name'])
      print('Email',sr.cleaned_data['email'])
      print('Password',sr.cleaned_data['password'])
      print('Password(again)',sr.cleaned_data['rpassword'])
  else:
    sr=StudentRegistration()
    print('Data not inserted :......')
  return render(request,'passchk/passchk.html',{'form':sr})
