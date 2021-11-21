from django.shortcuts import render
from django.views.generic import TemplateView

class ProfileTemplate(TemplateView):
  template_name='registration/profile.html'
