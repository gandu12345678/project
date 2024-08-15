from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    otp = models.IntegerField(null=True,blank=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    
    objects = UserManager()