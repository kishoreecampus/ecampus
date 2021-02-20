from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User




# Create your models here.
class Profile(models.Model):
    trust_name = models.CharField('Trust Name', max_length=60)
    institution_name = models.CharField('Institution Name', max_length=60)
    address1 = models.CharField('Address1', max_length=300)
    address2 = models.CharField('Address2', max_length=300)
    phone_number = PhoneNumberField()
    administrator = models.CharField('Administrator', max_length=300)
    mobile_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created by')
 
 
class RoomManagement(models.Model):
    
    pass

class ClassGroup(models.Model):
    class_group = models.CharField(unique=True, max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')
    

class ClassName(models.Model):
    class_group = models.ForeignKey(ClassGroup, on_delete=models.PROTECT, related_name='choose_classgroup')
    class_name = models.CharField(unique=True, max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')

class Section(models.Model):
    class_name = models.ForeignKey(ClassName, on_delete=models.PROTECT, related_name='choose_classname')
    section_name = models.CharField(unique=True,max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')


class Category(models.Model):
    category = models.CharField(unique=True, max_length=20)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')

class Caste(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='choose_category')
    caste = models.CharField(unique=True, max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')

 


