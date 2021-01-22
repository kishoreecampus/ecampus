from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission

class Employee(AbstractUser):
    email = models.EmailField('Email Address', unique=True)
    mobile = models.CharField(max_length=12, null=True, unique=True)
    modules = models.CharField('Accessable Modules', max_length=250, default=0)

class Department(models.Model):
    name = models.CharField('Department', max_length=120)

Group.add_to_class('department', models.ForeignKey(Department, on_delete=models.PROTECT, max_length=180))
