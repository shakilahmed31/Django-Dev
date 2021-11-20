from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class StudentRegistration(forms.Form):
  name=forms.CharField(validators=[validators.MaxLengthValidator(10)])
  email=forms.EmailField(max_length=20)
  password=forms.CharField(widget=forms.PasswordInput())

 