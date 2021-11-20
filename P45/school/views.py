from django.http import request
from django.shortcuts import render

from django.views.generic.base import TemplateView

class ChildClass(TemplateView):
  template_name='school/home.html'

  def get_context_data(self, **kwargs):

      context = super().get_context_data(**kwargs)
      context['name'] ='Sabia'
      context['roll'] =101
      #context={'name':'Sabia' ,'roll':'101'}
      return context
  