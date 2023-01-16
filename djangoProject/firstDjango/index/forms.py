from django.contrib.auth.models import User as DjangoUser

from django.forms import ModelForm, Form, CharField, PasswordInput, EmailInput, ValidationError
from index.models import User
import hashlib
# ввод данных пользователя
from datetime import date

class LoginForm(Form):
    username = CharField(label='Username', widget=EmailInput())
    password = CharField(label='Password', widget=PasswordInput())
 # валидация
    def clean_password(self):
        if len(self.data['password']) < 4:
            raise ValidationError('Password is too short')
        return self.data['password']
    def clean_email(self):
        if len(self.data['username']) < 5:
            raise ValidationError('Email is too short')
        return self.data['password']

    def clean(self):
        data = self.cleaned_data
        if 'username' in data and 'password' in data:
            if not data['username'] == 'admin' and data['password'] == 'root':
                raise ValidationError('You do not look like a real admin')
        else:
            raise ValidationError('Please,enter correct data')
        return data
# форма для регистрации пользователя
class UserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

# создаем пароль для пользователя
    def clean_password(self):
        if self.data['password']:
            _user = DjangoUser()
            _user.set_password(self.data['password'])
            return _user.password

        else:
            raise ValidationError('Not understand')

