from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, Widget

class Sign_Up_Form(UserCreationForm):
  password2=forms.CharField(label='confirm(again)',widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['username','last_name','email']
    labels={'email':'eMaiL'}


