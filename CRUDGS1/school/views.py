from django.shortcuts import render ,HttpResponseRedirect
from .forms import StudentForm
from . models import StudentRegistration

#Reading Part Done under this function
def home_view(request):
  fm=StudentRegistration.objects.all()
  return render(request,'school/home.html',{'form':fm})

#Create Part Done under this function
def create_view(request):
  if request.method=='POST':
    fm=StudentForm(request.POST)
    if fm.is_valid():
      fm.save()
    fm=StudentForm()
  else:
    fm=StudentForm()
  return render(request,'school/create.html',{'form':fm})

def del_view(request,id=0):
  if request.method=='POST':
    tm=StudentRegistration.objects.get(pk=id)
    tm.delete()
    return HttpResponseRedirect('/create/')

