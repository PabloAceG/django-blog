from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        """ 
        Gives space for configurations and keeps configurations in one place
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        