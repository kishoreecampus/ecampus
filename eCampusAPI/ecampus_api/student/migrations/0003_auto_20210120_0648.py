# Generated by Django 3.1.4 on 2021-01-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210120_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdocument',
            name='other_document_1',
            field=models.FileField(null=True, upload_to='uploads/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='studentdocument',
            name='other_document',
            field=models.ImageField(null=True, upload_to='uploads/', verbose_name='Photo'),
        ),
    ]