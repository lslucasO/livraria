
from django.contrib import admin
from django.urls import path
from library import views
from project import settings
from django.conf.urls.static import static

app_name = 'library'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)