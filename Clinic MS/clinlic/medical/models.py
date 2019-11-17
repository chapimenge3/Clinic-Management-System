from django.db import models
from django.core.validators import MinValueValidator
from django.utils.timezone import now
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from authe.models import User


class Token(models.Model):
	token_num = models.PositiveIntegerField(default= 1,verbose_name="id",validators=[MinValueValidator(1)],unique=True)
	token = models.CharField(verbose_name="Pre id",default="cms",max_length=50)
	def __str__(self):
		 return str(self.token) + str(self.token_num).zfill(5)

# class Record(models.Model):
# 	user = models.ManyToManyField(verbose_name="User",User)
# 	record = models.TextField(verbose_name="Description")
# 	register_date = models.DateField(default = now )

class Patient(models.Model):
	# token = models.OneToOneField(Token, on_delete=models.CASCADE, unique =True)
	first_name = models.CharField(verbose_name="First Name", max_length=50)
	last_name = models.CharField(verbose_name="Last Name", max_length=50)
	email = models.EmailField(verbose_name = "Email", max_length=254, blank=True,default="pa@pt.com")
	phone = PhoneNumberField(verbose_name ="Phone" ,blank=True, null=True)
	birth_date = models.DateField(default=now,verbose_name="Birth Date")
	sex = models.CharField(max_length=200, choices=(('Male', 'Male'), ('Female', 'Female')))
	photo = models.ImageField(blank=True, upload_to='', default='null.png')
	register_date = models.DateField (default = now )
	
	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150"/>' % self.photo.url)
	image_tag.short_description = 'Photo'
	image_tag.allow_tags = True
	def __str__(self):
		return self.first_name + ' ' + self.last_name
class PatientQueue(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.SET_NULL ,null=True)
	doctor =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	is_appointment = models.BooleanField(blank=True,default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	appointment_time = models.DateTimeField(auto_now_add=True)
	note = models.CharField(verbose_name="Your Note",default="Patient Queue",blank=True, max_length=100)

	
class Drug(models.Model):
	name = models.CharField(verbose_name="Drug Name", max_length=50,unique=True)
	price = models.PositiveIntegerField(verbose_name="Price Of Drug",default=0)
	description = models.TextField(verbose_name="Description")
	def __str__(self):
		return self.name
class MedicalHistory(models.Model):
	histroy = models.TextField(verbose_name="Medical History")
	doctor =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	patient = models.ForeignKey(Patient, verbose_name= "Patient", on_delete=models.SET_NULL,null=True)
	date_of_record = models.DateTimeField(auto_now_add=True)
		