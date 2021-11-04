from django import forms

class StudentRegistration(forms.Form):
  name=forms.CharField(error_messages={'required':'Enter Your name Shakil'})
  email=forms.EmailField(error_messages={'required':'Enter Your name Shakil'})
  password=forms.CharField(widget=forms.PasswordInput())