
from django.contrib import admin
from django.urls import path, include
from library import views
from project import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('users/', include('users.urls')),
]


