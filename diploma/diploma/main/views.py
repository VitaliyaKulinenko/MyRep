from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_control, cache_page
from django.views.generic import CreateView

from .models import Timetable, Blog
from rest_framework_swagger.views import get_swagger_view




# @cache_page(timeout=3600)
# @cache_control(public=True)
def index(request):
    timetable = Timetable.objects.all()
    return render(request, 'main/index.html', {'title': 'IKboxing','timetable': timetable})


def about(request):
    blog = Blog.objects.all()
    return render(request, 'main/about.html', {'title': 'IKboxing',
                                               'blog': blog})


def registration(request):
    return HttpResponse("здесь будет регистрация")


def enter(request):
    return render(request, 'main/enter.html')


def contacts(request):
    return HttpResponse("здесь будут контакты")


# schema_view = get_swagger_view(title='Pastebin API')






# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'main/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Registration")
#         return dict(list(context.items()+list(c_def.items())))



