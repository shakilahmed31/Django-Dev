from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput

class StudentRegistration(forms.Form):
  name=forms.CharField(max_length=20)
  password=forms.CharField(widget=forms.PasswordInput())
  rpassword=forms.CharField(label='paswword again',widget=forms.PasswordInput())

  def clean(self):
    cleaned_data=super().clean()
    vpass=self.cleaned_data['password']
    rvpass=self.cleaned_data['rpassword']
    if vpass!=rvpass:
       raise ValidationError('Password Mismatched !')
    