from django.contrib import admin
from django.urls import path, include
from library import views
from project import settings
from django.conf.urls.static import static
from . import views

app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'),
    path('register-create/', views.register_create, name='register-create'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login-create'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>', views.profile, name='profile'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
