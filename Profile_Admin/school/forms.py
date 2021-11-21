from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class Sign_Up_Form(UserCreationForm):
  password2=forms.CharField(label='confirm(again)',widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ['username','last_name','email']
    labels={'email':'eMaiL'}

class User_Change(UserChangeForm):
  password=None
  class Meta :
    model=User
    fields = ['username','last_name','email']

class Super_User_Change(UserChangeForm):
  password=None
  class Meta :
    model=User
    fields = '__all__'

