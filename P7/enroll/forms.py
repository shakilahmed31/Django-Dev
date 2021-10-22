from django import forms

class StudentRegistration(forms.Form):
  name=forms.CharField(max_length=50)
  email=forms.EmailField(max_length=30)
  mobile =forms.IntegerField(max_value=15)
