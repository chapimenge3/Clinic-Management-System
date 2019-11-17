from django import forms
from .models import User, Role
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import check_password
from django.contrib.admin.widgets import FilteredSelectMultiple


class SignUp(forms.ModelForm):
    password_regex = RegexValidator(
        regex=r'^\S{8,1024}',
        message='password must be at least 8 character'
    )
    user_password = forms.CharField(
        validators=[password_regex],
        max_length=1024,
        widget=forms.PasswordInput(),
        help_text='*Enter password minimum 8 character',
        label='Password'
    )
    confirm_password = forms.CharField(
        max_length=1024,
        widget=forms.PasswordInput(),
        help_text='*Confirm password'
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'sex', 'user_password',
                  'confirm_password',  'photo']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        cleaned_data.get('user_password')
        confirm = cleaned_data.get('confirm_password')
        sex = cleaned_data.get('sex')
        email = cleaned_data.get('email')

        if (not username) or (not first_name) or (not last_name) or (not sex) or (not user_password) or (not confirm):
            raise forms.ValidationError("Please correct the errors below.")
        if user_password and confirm:
            if user_password != confirm:
                raise forms.ValidationError("password is not confirmed")

        return cleaned_data