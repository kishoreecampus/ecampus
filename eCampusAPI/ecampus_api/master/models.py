from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Validators
trust_name_validator = RegexValidator(r'^[a-zA-Z ]+$', 'only valid trust name is required')
institution_name_validator = RegexValidator(r'^[a-zA-Z ]+$', 'only valid institution name is required')
address_validator = RegexValidator(r'^(\w *\s*[\  # \-\,\/\.\(\)\&]*)+$', 'only valid address is required')
class_group_validator = RegexValidator(r'^[a-zA-Z- ]+$', 'only valid class group is required')
class_name_validator = RegexValidator(r'^[a-zA-Z0-9- ]+$', 'only valid class name is required')
section_name_validator = RegexValidator(r'^[a-zA-Z0-9- ]+$', 'only valid section name is required')
category_validator = RegexValidator(r'^[a-zA-Z0-9-/() ]+$', 'only valid category is required')
caste_validator = RegexValidator(r'^[a-zA-Z() ]+$', 'only valid caste name is required')
academic_start_year = RegexValidator(r'\d{4}', 'only valid academic start year is required')
academic_end_year = RegexValidator(r'\d{4}', 'only valid academic end year is required')
# Create your models here.
class Profile(models.Model):
    trust_name = models.CharField('Trust Name', unique=True, max_length=60, validators=[trust_name_validator])
    institution_name = models.CharField('Institution Name', unique=True, max_length=60, validators=[trust_name_validator])
    address1 = models.CharField('Address1', max_length=300, validators=[address_validator])
    address2 = models.CharField('Address2', max_length=300, validators=[address_validator])
    phone_number = PhoneNumberField(unique=True)
    administrator = models.CharField('Administrator', max_length=300)
    mobile_number = PhoneNumberField(unique = True)
    academic_start_year = models.IntegerField(validators=[academic_start_year], null=True)
    academic_end_year = models.IntegerField(validators=[academic_end_year], null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created by')
 
 
class RoomManagement(models.Model):
    
    pass

class ClassGroup(models.Model):
    class_group = models.CharField(unique=True, max_length=100, validators=[class_group_validator])
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')
    

class ClassName(models.Model):
    class_group = models.ForeignKey(ClassGroup, on_delete=models.PROTECT, related_name='choose_classgroup')
    class_name = models.CharField(unique=True, max_length=100, validators=[class_name_validator])
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')

class Section(models.Model):
    class_name = models.ForeignKey(ClassName, on_delete=models.PROTECT, related_name='choose_classname')
    section_name = models.CharField(max_length=100, validators=[section_name_validator])
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')


class Category(models.Model):
    category = models.CharField(unique=True, max_length=20, validators=[category_validator])
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')

class Caste(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='choose_category')
    caste = models.CharField(unique=True, max_length=100, validators=[caste_validator])
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.IntegerField('created_by')

 


