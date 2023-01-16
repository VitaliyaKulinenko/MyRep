# список маршрутов
from .views import (
    index_page,about_page111,all_instances, sign_up
)
from index.views import UserAPI
# from index.urls import urlpa
from django.urls import include
urlpatterns = [
    path('', index_page),
    path('about/', about_page111),
    path('all-instances', all_instances),
    path('login', about_page111, name='login'),
    path('sign-up', sign_up, name='sign_up' ),
    path('user', UserAPI.as_view(), name='user' ),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

urlpatterns = format.suffix_patterns(urlpatterns)