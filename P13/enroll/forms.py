from django import forms
from . models import User 


class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("sname","email","password")

class TeacherRegistration(StudentRegistration):
    
    class Meta(StudentRegistration.Meta):
        fields = ("tname","email","password")
