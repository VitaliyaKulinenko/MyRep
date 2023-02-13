from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form, CharField, PasswordInput, ValidationError, TextInput, DateTimeInput, Textarea
from django.contrib.auth.models import User as DjangoUser
from .models import *
import hashlib


class UserForm(ModelForm):

    class Meta:
        model = DjangoUser
        fields = ['username', 'email', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'

            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'

            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            })

        }

    def clean_password(self):
        if self.data['password']:
            _user = DjangoUser()
            _user.set_password(self.data['password'])
            return _user.password
        else:
            raise ValidationError("Don't understand You")




class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name'

            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Review'

            }),


        }


class LoginForm(Form):
    username = CharField(label='Username')
    password = CharField(label='Password', widget=PasswordInput())

    def clean(self):
        data = self.cleaned_data
        if 'username' not in data or 'password' not in data:
            raise ValidationError('Please,try again')
        return data


