from django.shortcuts import render
from . forms import UserForm


def show_view(request):
  if request.method=='POST':
    uf=UserForm(request.POST)
    if uf.is_valid():
      print('valid data')
      uf=UserForm()

  else:
    uf=UserForm()
  return render(request,'Modelform/index.html',{'form':uf})
