from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required = True, help_text = "Enter your email")
    class Meta:
        model = User
        fields = ['username','email','password1','password2']