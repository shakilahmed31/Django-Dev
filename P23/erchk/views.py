from django.shortcuts import render
from . forms import StudentRegistration
from .models import User

def stu_view(request):
  if request.method=='POST':
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
      print('Valid SR')
      n1=sr.cleaned_data['name']
      e1=sr.cleaned_data['email']
      p1=sr.cleaned_data['password']
      #mr=User(id=1,name=n1,email=e1,password=p1)
      #mr.save()
      mr=User(id)
      mr.delete()
      sr=StudentRegistration()
      #print('Name :', n1 , 'Email :', e1)

  else:
    sr=StudentRegistration()
    print('else working ')
  return render(request,'erchk/index.html',{'disp':sr})
