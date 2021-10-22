from django import forms
from django.core import validators




class StudentRegistration(forms.Form):
  name=forms.CharField(max_length=30)
  email=forms.EmailField(max_length=20)
  password=forms.CharField(widget=forms.PasswordInput)
  rpassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput)

  def clean(self):
    clean_data=super().clean()
    valpwd=clean_data['password']
    rvalpwd=clean_data['rpassword']
    if valpwd!=rvalpwd:
      raise forms.ValidationError('Password not Matched')
    