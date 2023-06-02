from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm #prebuilt form
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta: #we will define in this class that RegisterForm class is going to save into the user database
        model=User
        fields= ["username", "email", "password1", "password2"]
