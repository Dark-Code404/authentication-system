from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *



class UserRegisterForm(UserCreationForm):
   

    class Meta:
        model=CusUser
        fields=['username','email','password1','password2','role']


class UserLoginForm(forms.Form):   
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))  
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))  
        

