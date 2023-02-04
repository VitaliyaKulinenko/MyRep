from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import CreateView

from .forms import *
from .models import Timetable, Blog
# from rest_framework_swagger.views import get_swagger_view


# @cache_page(timeout=3600)
# @cache_control(public=True)
def index(request):
    timetable = Timetable.objects.all()
    return render(request, 'main/index.html', {'title': 'IKboxing', 'timetable': timetable})


def about(request):
    blog = Blog.objects.all()

    return render(request, 'main/about.html', {'title': 'IKboxing', 'blog': blog})








def contacts(request):
    return HttpResponse("здесь будут контакты")


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about-me')
    else:
        form = UserForm()
    return render(request, 'main/register.html', {'form': form})


def enter(request):
    error = ''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(password=data['password'], username=data['username'])
            if user is not None:
                login(request, user)
                return redirect('about-me')
            else:
                return redirect('enter')
        else:
            error = 'ERROR!'
    else:
        form = LoginForm()
    return render(request, 'main/register.html', {
        'form': form,
        'error': error,
    })


def addpost(request):
    form = PostForm()

    reviews = Reviews.objects.all()
    return render(request, 'main/addpost.html', {'form': form, 'title': 'Leave your feedback'})




