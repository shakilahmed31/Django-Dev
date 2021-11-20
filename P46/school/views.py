from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView

class SelfDefine(RedirectView):
  url='https://www.google.com'

class SelfDefine1(RedirectView):
  pattern_name='mindex'
