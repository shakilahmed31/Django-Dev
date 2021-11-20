from django import forms

class StudentRegistration(forms.Form):
  name=forms.CharField(max_length=20)
  email=forms.EmailField(max_length=20)

  def clean_name(self):
    valname=self.cleaned_data['name']
    if len(valname)<4:
      raise forms.ValidationError ('You name is too short 4 ch only')
    return valname