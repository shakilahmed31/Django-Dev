from django import forms
from django.core import validators


class StudentRegistration(forms.Form):
  name=forms.CharField(error_messages= {'required':'Put your Name'})
  email=forms.EmailField(error_messages={'required':"pur your email"})
  password=forms.CharField(widget=forms.PasswordInput ,error_messages={'required':'put your password'})