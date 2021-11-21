
from django import forms
class StudentRegistration(forms.Form):
  name=forms.CharField(error_messages={'required':'Sabia you did mistake '})
  password=forms.EmailField(error_messages={'required':'oh No Sabia you forget to put your password'})
 
