from django import forms


class StudentRegistration(forms.Form):
  name=forms.CharField(max_length=30)
  email=forms.EmailField(max_length=30)
  password=forms.CharField(widget=forms.PasswordInput)