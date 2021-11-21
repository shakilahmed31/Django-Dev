
from django.shortcuts import render

def setsession(request):
  d1=request.session['n1']='Sabia'
  d2=request.session['n2']='Arosh'
  return render(request,'student/setsession.html',{'n1':d1,'n2':d2})

def getsession(request):
  #n1=request.session['n1']
  #another way to get is 
  nm=request.session.get('n1',default='Guest')
  nm1=request.session.get('n2',default='Guest')
  #if there is no value on get in that case default value display 
  return render(request,'student/getsession.html',{'disp':nm ,'disp1':nm1})

def delsession(request):
  if 'n1' in request.session:
    del request.session['n1']  
  return render(request,'student/delsession.html')