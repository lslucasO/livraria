from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    ...
    
    
admin.site.register(Profile, ProfileAdmin)