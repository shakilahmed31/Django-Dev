from django.shortcuts import render


# Create your views here.

def app1_func(request):
  par= "App1"
  return render(request,'app1/App1.html',{'param':par})

