from django.shortcuts import render
from . forms import SignUpForm


def signup_view(request):
  if request.method=='POST':
    uf=SignUpForm(request.POST)
    if uf.is_valid():
      uf.save()
  else:
    uf=SignUpForm()
  return render(request,'appauth/Signup.html',{'disp':uf})


