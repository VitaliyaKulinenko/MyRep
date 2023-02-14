from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import CreateView

from .forms import *
from .models import Timetable, Blog
# from rest_framework_swagger.views import get_swagger_view
from .forms import *


# @cache_page(timeout=3600)
# @cache_control(public=True)
def index(request):
    timetable = Timetable.objects.all()
    return render(request, 'main/index.html', {'title': 'IKboxing', 'timetable': timetable})


def about(request):
    blog = Blog.objects.all()

    return render(request, 'main/about.html', {'title': 'IKboxing', 'blog': blog})


def contacts(request):
    return render(request, 'main/contacts.html',  {'title': 'IKboxing'})


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'main/register.html', {'form': form})


def log_in(request):
    error = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(password=data['password'], username=data['username'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('registration')
        else:
            error = 'ERROR!'
    else:
        form = LoginForm()
    return render(request, 'main/enter.html', {
        'form': form,
        'error': error,
    })



def log_out(request):
    logout(request)
    return redirect('home')


def addpost(request):
    # form = PostForm()
    reviews = Reviews.objects.all()
    return render(request, 'main/addpost.html', {'title': 'IKboxing', 'reviews': reviews})


def formaddpost(request):
    error = ''
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
        else:
            error = 'Неверно заполнено, попробуйте еще раз'
    form = ReviewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/formaddpost.html', data)





