from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

_UNSAVED_1,  _UNSAVED_2, _UNSAVED_3 = 'unsaved_1', 'unsaved_2', 'unsaved_3'

def get_upload_path(instance, file_name):
    return "uploads/documents/{0}/{1}".format(instance.pk, file_name)

class Student(models.Model):
    pass

class Document(models.Model):
    student = models.OneToOneField(Student, on_delete=models.PROTECT, null=True)
    student_photo = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    birth_certificate = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    tc = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    other_document = models.ImageField('Photo', upload_to=get_upload_path, validators=[FileExtensionValidator(['png','jpg','jpeg'])], null=True)
    uploaded_on = models.DateTimeField('Uploaded On', auto_now_add=True)


@receiver(pre_save, sender=Document)
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk:
        if not hasattr(instance, _UNSAVED_1):
            setattr(instance, _UNSAVED_1, instance.student_photo)
            instance.student_photo = None
        if not hasattr(instance, _UNSAVED_2):
            setattr(instance, _UNSAVED_2, instance.birth_certificate)
            instance.birth_certificate = None
        if not hasattr(instance, _UNSAVED_3):
            setattr(instance, _UNSAVED_3, instance.tc)
            instance.tc = None

@receiver(post_save, sender=Document)
def save_file(sender, instance, created, **kwargs):
        if created:
            if hasattr(instance, _UNSAVED_1):
                instance.student_photo = getattr(instance, _UNSAVED_1)
            if hasattr(instance, _UNSAVED_2):
                instance.birth_certificate = getattr(instance, _UNSAVED_2)
            if hasattr(instance, _UNSAVED_3):
                instance.tc = getattr(instance, _UNSAVED_3)
            instance.save()
            # delete it if you feel uncomfortable...
            instance.__dict__.pop(_UNSAVED_1)
            instance.__dict__.pop(_UNSAVED_2)
            instance.__dict__.pop(_UNSAVED_3)