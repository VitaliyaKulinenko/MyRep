from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form, CharField, PasswordInput,ValidationError

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

class PostForm(ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'content']


class LoginForm(Form):
    username = CharField(label='Username')
    password = CharField(label='Password', widget=PasswordInput())

    def clean(self):
        data = self.cleaned_data
        if 'username' not in data or 'password' not in data:
            raise ValidationError('Please,try again')
        return data


