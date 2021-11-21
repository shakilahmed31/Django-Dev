from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .forms import StudentForm

class StudentCreateView(CreateView):
  form_class =StudentForm
  template_name='school/student_form.html'

  # def get_form(self):
  #   form = super().get_form()
  #   form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
  #   form.fields['password'].widget = forms.PasswordInput(attrs={'class':'myclass'})
  #   return form 

class ThankYou(TemplateView):
  template_name='school/thankyou.html'

