from django.shortcuts import render
from django.views import View
from . forms import Contactform
from django.http import HttpResponse

def func_view(request):
  return render(request,'school/home.html')

class class_view(View):
  def get(self,request):
    return render(request,'school/home.html')

def about(request):
  context={'msg':'welcome to my functionbase view '}
  return render(request,'school/about.html',context)

class About_view(View):
  def get(self,request):
    context={'msg':'welcome to my ClassBase view '}
    return render(request,'school/about.html',context)

def conttactform(request):
  if request.method=='POST':
    form=Contactform(request.POST)
    if form.is_valid():
      print(form.cleaned_data['name'])
      return HttpResponse('Thank You form Submitted !!')
  else:
    form=Contactform() 
  return render(request,'school/contact.html',{'fm':form})

class ContactForm(View):
  def get(self,request):
    form=Contactform()
    return render(request,'school/contact.html',{'fm':form})
    
  def post(self,request):
    form=Contactform(request.POST)
    if form.is_valid():
      print(form.cleaned_data['name'])
      return HttpResponse('Thank You form Submitted Class Form!!')

def news(request,tempalte_name):
  #path_variable='school/news.html'
  path_variable=tempalte_name
  context={'news':'This chapter covers function and views'}
  return render(request,path_variable,context)

    
