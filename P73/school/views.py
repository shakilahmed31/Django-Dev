from django.shortcuts import render
from django.views.generic.base import TemplateView ,RedirectView


class RedirectTest(RedirectView):
  url='https://www.cnn.com'

class RedirectTest2(RedirectView):
  url='/'
