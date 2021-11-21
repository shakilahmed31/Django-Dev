from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ContactForm,FeedbackForm
from django.views.generic.edit import FormView

class ContactFormView (FormView):
  template_name='school/contact.html'
  form_class =ContactForm
  success_url= '/thankyou/'

class Feedbackformview(FormView):
  template_name='school/contact.html'
  form_class = FeedbackForm
  success_url= '/thankyou/'

class ThanksTemplateView(TemplateView):
  template_name='school/thankyou.html'
  
