from django.shortcuts import render ,HttpResponse
from . forms import Sign_Up_Form
from django.contrib import messages


def signup(request):
  if request.method=='POST':
    ucform=Sign_Up_Form(request.POST)
    if ucform.is_valid():
      messages.success(request,'Account Created !!!')
      ucform.save()
      messages.success(request,'Account Created !!!')

      #return HttpResponse('Successfully Submitted')
  else:
    ucform=Sign_Up_Form()
  return render(request,'school/index.html',{'form':ucform})
