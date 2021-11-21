from django import forms
from .models import StudentRegistration

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ("id","name","roll","email","password")