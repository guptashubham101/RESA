from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForm(UserCreationForm):
	username = forms.CharField(max_length=255)
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)
	email = forms.CharField(max_length=255)
	contact_number = forms.CharField(max_length=255)
	# def clean(self):
	# 	cleaned_data = super().clean()
	# 	submitted_username = cleaned_data.get('username')
	# 	submitted_password = cleaned_data.get('password1')
	# 	if submitted_username == submitted_password:
	# 		raise ValidationError(
	# 			"Your password cannot be your username.", code="invalid_password"
				# )
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "contact_number","password1", "password2")
    
