from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from django import forms
from ask_ermakov.models import *

class RegistrationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
	class Meta:
		model = User
		fields = ("username", "email")
	def save(self, commit=True):
		obj = super(RegistrationForm, self).save(commit=False)
		obj.username = self.cleaned_data["username"]
		obj.email = self.cleaned_data["email"]
		if commit:
			obj.save()
		return obj

class RegistrationProfileForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(RegistrationProfileForm, self).__init__(*args, **kwargs)
		self.fields['avatar'].required = False
	class Meta:
		model = Profile
		fields = ("avatar",)
	def save(self, user, commit=True):
		obj = super(RegistrationProfileForm, self).save(commit=False)
		obj.user = user
		if commit:
			obj.save()
		return obj