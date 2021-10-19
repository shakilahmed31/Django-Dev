from django.shortcuts import render


def home_view(request):
  
  return render(request,'mainp/home.html')


def about_view(request):
  
  return render(request,'mainp/about.html')
