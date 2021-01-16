from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField('Email Address', unique=True)
    modules = models.CharField('Accessable Modules', max_length=250, default=0)

