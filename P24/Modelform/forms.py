from . models import User
from django import forms


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("name","email","password")
        labels={'name':'Enter Name','email':'Enter Your email','password':"password can not be empty"}
        error_messages={'name':{'required':'Doya kore nam likhun'},
                'password':{'required':'Aponi vule gesen password dite'}}
