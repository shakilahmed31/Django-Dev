from django.shortcuts import render
from django.views.generic.base import TemplateView
from . models import Student
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView

class Student_View(CreateView):
  model=Student
  fields=['name','email','password']
  success_url='/done/'

class ThankYou(TemplateView):
  template_name='school/thankyou.html'

class UpdateView(UpdateView):
  model=Student
  fields=['name','email','password']
  success_url='/done/'
  
class display_view(Student_View):
    template_name='school/display.html'
    def get(self,request):
      fm=Student.objects.all()
      print('check fm', fm)
      return render(request,self.template_name,{'fm':fm})

class StudentDeleteView(DeleteView):
  model=Student
  fm=Student.objects.all()
  print('under delete class :',fm)
  success_url='/create/'