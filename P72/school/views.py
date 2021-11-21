from django.shortcuts import render
from django.views.generic.base import TemplateView

#class HometemplateView(TemplateView):
#  template_name= 'school/home.html'

#class HometemplateView(TemplateView):
#  template_name= 'school/home.html'
#  def get (self , request):
#    context={'info':"context passing from views"}
#    return render(request,self.template_name,context)

class HometemplateView(TemplateView):
  template_name= 'school/home.html'
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['name']='Sabia'
      context['roll']='101'
      #context={'name':'Sabia','roll':'101'}
      print(kwargs)

      return context
    
 



