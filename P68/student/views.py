from django.shortcuts import render

def setsession(request):
  d1=request.session['n1']='Sabia'
  d2=request.session['n2']='Arosh'
  return render(request,'student/setsession.html')

def getsession(request):
  nm=request.session.get('n1')
  keys=request.session.keys()
  items=request.session.items()
  age=request.session.setdefault('age','27')
  return render(request,'student/getsession.html',{'disp':nm ,'keys':keys, 'item':items })

def delsession(request):
  #if 'n1' in request.session:
   # del request.session['n1']
  request.session.flush()  # to remove complete data
  return render(request,'student/delsession.html')