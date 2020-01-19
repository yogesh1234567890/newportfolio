from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from hello.models import Photos,login

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields=['logo_image','first_image','second_image']

class Form(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model =login
        fields=['username','password']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']