from django.contrib import admin
from .models import Token
from .models import *
from django.utils.safestring import mark_safe
from django import forms

class PatientCreationForm(forms.ModelForm):
   class Meta:
        model = Patient
        fields = ( 'first_name', 'last_name','email',  'phone', 'sex', 'photo', 'register_date')
   def save(self, commit=True):
      patient = super().save(commit=False)
      if commit:
         patient.save()
      return patient
        
class PatientAdmin(admin.ModelAdmin):
   form = PatientCreationForm
   add_form = PatientCreationForm
   list_display = ('first_name','last_name','id' )
   list_filter = ('sex',)
   fieldsets = (
            ('Info', {
                "fields": ('first_name' , 'last_name','email','sex'),
            }),
            ('Profile' ,{
               'fields' : ('phone','email', 'image_tag' ,'photo' , )
            }),
            ('Date', {
               'fields': ('register_date',)
            })
        )
   readonly_fields = ('image_tag',)
   add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'first_name', 'last_name','email', 'sex', 'phone', 'image_tag', 'photo', 'register_date')}
        ),
   )
   search_fields = ('email',)
   ordering = ('first_name',)
class TokenAdmin(admin.ModelAdmin):
   class Meta:
        model = Token
        fields = ('token_num',)
   def save(self,commit=True):
      token = super().save()
      return token
class PatientQ(admin.ModelAdmin):
   class Meta:
      model = PatientQueue
   ordering = ('appointment_time',)
class MedicalHistoryCreationForm(forms.ModelForm):
   class Meta:
        model = MedicalHistory
        fields = ( 'patient', 'doctor','histroy')
   def save(self, commit=True):
      medical_history = super().save(commit=False)
      if commit:
         medical_history.save()
      return medical_history
class MedicalHistoryAdmin(admin.ModelAdmin):
   form = MedicalHistoryCreationForm
   add_form = MedicalHistoryCreationForm
   list_display = ('patient','doctor','id' ) 
   fieldsets = (
      ('Patient', {'fields':'patient'}) ,
      ('Doctor', {'fields' : 'doctor'} ),
      ('Info' , {'fields' : ('histroy' , 'date_of_record')})
   )
  
   ordering = ('date_of_record',)
admin.site.register(MedicalHistory)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(PatientQueue,PatientQ)
