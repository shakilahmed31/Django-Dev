from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Under function based view autometically get method call when urls hit
def myview(request):
  return HttpResponse('<H1>This is function Based</H1>')

# under clas base view we need to mention get method 
class MyView(View):
  name='Sabia'
  def get(self,request):
    #return HttpResponse('<H1>This is Class Based View</H1>')
    return HttpResponse(self.name)

class MyViewChild(MyView):
  def get(self,request):
    return HttpResponse(self.name)