
from django import forms
class StudentRegistration(forms.Form):
  name=forms.CharField(label='Your Name',
  label_suffix=" " , initial= ' Shakil',
  required=False , disabled=True ,
  help_text="guiding for input ")
  email=forms.EmailField()
  mobile=forms.IntegerField()
  key=forms.CharField(widget=forms.HiddenInput())

# <p><label for="id_name">Your Name </label> <input type="text" 
# name="name" value=" Shakil" disabled id="id_name">
# <span class="helptext">guiding for input </span></p>

## Label : what ever we write here it will display webpage
        #and change view source as same
#initil : what we write it will display on web page box 
#suffix : what we put inside it will display output
#helptext : it will display beside box for guiding users 
#required be defauls True for input , if we write false it will be disable