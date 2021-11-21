from django.shortcuts import render
from . forms import StudentRegistration
from django.contrib import messages

def regi(requests):
  if requests.method=='POST':
    fm=StudentRegistration(requests.POST)
    if fm.is_valid():
      fm.save()
      #messages.add_message(requests,messages.INFO, "Successfully Created")
      messages.success(requests,"your account Creted ")
      messages.info(requests, "you have created successfully")
      messages.warning(requests,"your account Creted Warning ")
      messages.error(requests, "you have created successfully Error")
      
      #messages.debug(requests,"this is Debug")
      #messages.set_level(requests,messages.DEBUG)
      #messages.debug(requests,"This is New Debug")
      print("Shakil Msg",messages.get_level(requests))
      fm=StudentRegistration()
  else:
    fm=StudentRegistration()
  return render(requests,'enroll/userregistration.html',{'form':fm})

