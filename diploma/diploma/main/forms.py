from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import *


class UserForm(ModelForm):

    class Meta:
        model = Registration
        fields = ['user_name', 'email', 'password']

    # def clean_password(self):
    #     if self.data['password']:
    #         _user = Registration()
    #         _user.set_password(self.data['password'])
    #         return _user.password
    #     else:
    #         raise ValidationError ("Don't understand You")
