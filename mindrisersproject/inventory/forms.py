from django import forms 
from core.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegisterForm(UserCreationForm):
    email =forms.EmailField()
    class Meta:
        model =User
        fields = ['username','email','password','password2']