from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponseRedirect

def student_view(request):
  if request.method=='POST':
    sr=StudentRegistration(request.POST)
    if sr.is_valid():
      print('before else:',sr)
      
      print('Last IF:',sr)
      n1=sr.cleaned_data['name']
      e1=sr.cleaned_data['email']
      print('clened data:',n1 , 'and email :', e1 )
      #sr=StudentRegistration()
      print('after execution:', sr)
      #return render(request,'app1/cong.html',{'nm':n1}) 1st way of showing succesfully data created
      return HttpResponseRedirect ('/cong/')

      
  else:
    sr=StudentRegistration()
    print('Else:',sr)
  return render(request,'app1/index.html',{'disp':sr})

def thank_view(request):
  return render(request,'app1/cong.html')