from django import forms
from django.core.validators import RegexValidator
from .models import Patient

class RegisterPatient(forms.ModelForm):
   class Meta:
      model = Patient
      fields = ['first_name','last_name','email','phone','birth_date','sex','photo']
   
   def clean(self):
      cleaned_data = super().clean()
      first_name = cleaned_data.get('first_name')
      last_name = cleaned_data.get('last_name')
      sex = cleaned_data.get('sex')
      birth_date = cleaned_data.get('birth_date')
      if (not first_name) or(not last_name)  or (not sex):
            raise forms.ValidationError("Please correct the errors below.") 
      return cleaned_data