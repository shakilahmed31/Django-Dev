from django.shortcuts import render ,HttpResponseRedirect
from .models import User
from .forms import RegistrationForm

def addandshow(request):
  if request.method == "POST":
    fm=RegistrationForm(request.POST)
    print('before cleam Shakil',fm)
    if fm.is_valid():
      nm=fm.cleaned_data['name']
      em=fm.cleaned_data['email']
      pm=fm.cleaned_data['password']
      print(' After clean Name Shakil :', nm , 'Email :',em ,'Password :', pm)
      reg=User(name=nm,email=em,password=pm)
      reg.save()
      fm=RegistrationForm()
  else:
    fm=RegistrationForm()
  stud=User.objects.all()
  return render(request,'school/addandshow.html',{'form':fm ,'stu':stud })

def student_del(request,id):
  if request.method=='POST':
    pi=User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

def student_update(request ,id ):
  if request.method == 'POST':
    pi=User.objects.get(pk=id)
    fm=RegistrationForm(request.POST,instance= pi)
    if fm.is_valid():
      fm.save()
  else:
    pi=User.objects.get(pk=id)
    fm=RegistrationForm(instance= pi)
  return render(request,'school/update.html',{'form':fm})
  
