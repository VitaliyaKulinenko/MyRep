
from django.urls import path
# . -значит эта же директория
from . import views
# здесь будем отслеживать,куда переходит пользователь
# from .views import RegisterUser

urlpatterns = [
    path('', views.index, name='home'),
    path('about-me', views.about, name='about'),
    path('registration', views.sign_up, name='registration'),
    path('enter', views.log_in, name='ent'),
    path('contacts', views.contacts),
    path('add_post', views.addpost, name='review'),
    path('formaddpost', views.formaddpost),
]
