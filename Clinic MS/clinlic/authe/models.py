from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

class Role(models.Model):
    role = models.CharField(max_length=200)
    short_name = models.CharField(max_length=10)
    def __str__(self):
        return self.short_name

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email,role, password):
        """
        Creates and saves a User with the given email 
        and <li ><a href="#">{{user.username}}</a></li>password.
        """
        if not username:
            raise ValueError('Users must have an user name')
        
        if not first_name:
            raise ValueError('Users must have an first name')

        if not last_name:
            raise ValueError('Users must have an last name')

        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            register_date=timezone.now().date(),
        )
        user.set_password(password)
        user.save(using=self._db)
        user.role.set([role])
        return user 
    role = Role.objects.get(short_name='admin')
    def create_superuser(self,username, email, password,role=role):
        """
        Creates and saves a superuser with the given email, password ...
        """
        
        user = self.create_user(
            username=username,
            first_name=' ',
            last_name=' ',
            email=email,
            role=role,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        user.role.set([role])
        return user

class User(AbstractBaseUser):
   username = models.CharField(verbose_name = "Username", max_length=50,unique=True,default="")
   first_name = models.CharField(verbose_name="First Name", max_length=50)
   last_name = models.CharField(verbose_name="Last Name", max_length=50,blank=True, null=True)
   email = models.EmailField(verbose_name = "Email", max_length=254,unique=True)
   phone = PhoneNumberField(blank=True, null=True)
   sex = models.CharField(max_length=200, choices=(('male', 'male'), ('female', 'female')))
   role = models.ManyToManyField(Role)
   photo = models.ImageField(blank=True, upload_to='', default='null.png')
   is_active = models.BooleanField(default=True)
   is_admin = models.BooleanField(default=False)
   register_date = models.DateField(default = now )
   is_dr = models.BooleanField(verbose_name="Is Doctor" ,default=False)
   profesion = models.CharField(verbose_name="Profession",default="NONE" , max_length=50)
   objects = UserManager()
   USERNAME_FIELD = 'username'
   REQUIRED_FIELDS = ['email']

   def image_tag(self):
      return mark_safe('<img src="%s" width="150" height="150"/>' % self.photo.url)

   image_tag.short_description = 'Photo'
   image_tag.allow_tags = True

   def __str__(self):
      return self.first_name + ' ' + self.last_name
   @property
   def getrole(self):
       return self.role
   def has_perm(self, perm, obj=None):
      "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
      return True
   def has_module_perms(self, app_label):
      "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
      return True
   @property
   def is_staff(self):
      "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
      return self.is_admin
   @property
   def get_role(self):
       return self.role
