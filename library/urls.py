from django.contrib import admin
from django.urls import path, include
from library import views
from project import settings
from django.conf.urls.static import static
from . import views

app_name = 'library'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('book-page/<int:id>', views.book_page, name='book-page'),
    path('create-account/', views., name='create-account'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
