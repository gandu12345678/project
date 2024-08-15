from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(UA):
    pass