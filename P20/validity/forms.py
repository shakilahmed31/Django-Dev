from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class StudentRegistration(forms.Form):
  name=forms.CharField(validators=[validators.MinValueValidator(4)])
  email=forms.EmailField(max_length=20)
  password=forms.CharField(widget=forms.PasswordInput())

  """def clean(self):
    cleaned_data=super().clean()
    valname=self.cleaned_data['name']
    valemail=self.cleaned_data['email']
    valpass=self.cleaned_data['password']
    if len(valname)<4:
      raise ValidationError("Name is short less len 4 character")
    valemail=self.cleaned_data['email']
    if len(valemail)<4:
      raise ValidationError("email is short less len 4 character")
    valpass=self.cleaned_data['password']
    if len(valpass)<5:
      raise ValidationError("Password is short less len 4 character")"""
    