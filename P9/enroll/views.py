from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

def thankyou(request):
  return render(request,'enroll/success.html')

def showdata(request):
  if request.method=="POST":
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
      name=sr.cleaned_data['name']
      print('this is from POST request')
      print(sr)
      #return render(request,'enroll/success.html',{'na':name})
      return HttpResponseRedirect('/regi/success/')


  else:
    sr=StudentRegistration()
    print('this is from get request')

  return render(request,'enroll/studentdata.html',{'form':sr})
