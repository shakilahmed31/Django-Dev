from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from . forms import ContactForm
from django.http import HttpRequest

def homefun(request):
  return render(request,'school/home.html')

class HomeClassView(View):
  def get (self,request):
    return render(request,'school/home.html')

### So This is conversion of function to class ###
### Now we will Pass context ####
def aboutfun(request):
  context ={'msg':'Message from function'}
  return render(request,'school/about.html',context)

class AboutClassView(View):
  
  def get (self,request):
    context ={'msg':'Message from ClassBased View'}
    return render(request,'school/about.html',context)

### now we will see POST method Example so we make forms### will see functionand class both view ###

def contact_view(request):
  if request.method=='POST':
    fm=ContactForm(request.POST)
    if fm.is_valid():
      print('function Form Working :', fm)
      return HttpResponse('<h2>Form Working under function </h2>')
  else:
    fm=ContactForm()
  return render(request,'school/contact.html',{'form':fm})

class ContactClassView(View):
  def get(self ,request):
    fm=ContactForm()
    return render(request,'school/contact.html',{'form':fm})
    ####as when first time call the function its get work so the code is for get ###
  def post (self ,request):
    if request.method=='POST':
      fm=ContactForm(request.POST)
      if fm.is_valid():
       print('function Form Working :', fm)
       return HttpResponse('<h2>Form Working under Class </h2>')

##########form concept claer under above discussion###########

def news(request ,template_name ):
  #template_name='school/news.html'  # This is one way of passing template as variable 
  template_name= template_name
  context={'info':'Most of the people fighting with Earning'}
  return render(request,template_name,context)
## in this example what we understand we can write tempalte as variable as well###
##in this way if we arite code we can use this view for another function###

class News(View):
  def get(self,request):
    context={'info':'Most of the people fighting with Earning class'}
    return render(request,'school/news.html',context)

class NewsClassView(View):
  #template_name='school/news.html'
  template_name = ''
  def get(self,request):
    #template_name='school/news.html' #This is one way1 
    context={'info':'Most of the people fighting with Earning'}
    #return render(request,template_name,context) #This is one way1
    #we can write template name under class as well but in that case we have to use self with the variable as python
    return render(request,self.template_name,context)