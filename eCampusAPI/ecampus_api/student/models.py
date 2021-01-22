from django.db import models
from preadmission.models import Application
from django.core.validators import FileExtensionValidator

class Student(models.Model):
    pass

def get_upload_path(instance, filename):
    return "uploads/documents/application_{0}/{1}".format(instance.application.id, filename)

class Document(models.Model):
    application = models.OneToOneField(Application, on_delete=models.PROTECT)
    student = models.OneToOneField(Student, on_delete=models.PROTECT, null=True)
    student_photo = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    birth_certificate = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    tc = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    other_document = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    uploaded_on = models.DateTimeField('Uploaded On', auto_now_add=True)
