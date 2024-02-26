from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_icon = models.ImageField(upload_to='profiles/icons/', blank=True, default='')
    bio = models.TextField(default='', blank=True)
