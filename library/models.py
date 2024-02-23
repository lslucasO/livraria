from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(unique=True, default='')
    author = models.CharField(max_length=55)
    price = models.FloatField()
    cover = models.ImageField(upload_to='library/covers/%Y/%m/%d/', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    avaliable_until = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
