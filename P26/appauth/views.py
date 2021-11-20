from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
  if request.method=='POST':
    uf=UserCreationForm(request.POST)
    if uf.is_valid():
      uf.save()
  else:
    uf=UserCreationForm()
  return render(request,'appauth/Signup.html',{'disp':uf})


