from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomeUserCreationForm(UserCreationForm):
    username=forms.CharField(max_length=150)
    email=forms.EmailField()
    password1=forms.CharField(),
    password2=forms.CharField()

    class Meta:
        model=User
        fields=('username','email','password1')
    