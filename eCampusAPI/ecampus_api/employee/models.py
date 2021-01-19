from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    email = models.EmailField('Email Address', unique=True)
    mobile = models.CharField(max_length=12, null=True, unique=True)
    modules = models.CharField('Accessable Modules', max_length=250, default=0)

