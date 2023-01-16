from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from diploma.diploma import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # при переходе на главную страницу будет вызываться приложение main
    path('', include('main.urls')),
    path('__debug__/', include('debug_toolbar.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)