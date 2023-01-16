
from django.urls import path
# . -значит эта же директория
from . import views
# здесь будем отслеживать,куда переходит пользователь

urlpatterns = [
    path('', views.index),
    path('about-me', views.about),
    # path('registration', RegisterUser.as_view(), views.registration),
    path('enter', views.enter),
    path('contacts', views.contacts),

]
