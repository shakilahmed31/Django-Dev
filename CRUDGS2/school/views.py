from django.shortcuts import render,redirect
from . models import Student
from . forms import StudentForm

def show_date(request):
  records=Student.objects.all()
  return render(request,'school/Show.html',{'disp':records})

def add_data(request):
  if request.method=='POST':
    fm=StudentForm(request.POST)
    if fm.is_valid():
      fm.save()
      print('check save data: ', fm.save())
  else:
    fm=StudentForm()
  return render(request,'school/add.html',{'form':fm})

def del_date(request,id=0):
  records=Student.objects.get(pk=id)
  print(records)
  records.delete()
  return redirect('/')

def update_data(request,id):
  if request.method=='POST':
    pi=Student.objects.get(id=id)
    fm=StudentForm(request.POST,instance=pi)
    if fm.is_valid():
      fm.save()
    return redirect('/')
  else:
    pi=Student.objects.get(id=id)
    fm=StudentForm(instance=pi)
  return render(request,'school/update.html',{'form':fm})

 



  
