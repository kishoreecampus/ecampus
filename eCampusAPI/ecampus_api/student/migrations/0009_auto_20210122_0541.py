# Generated by Django 3.1.4 on 2021-01-22 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preadmission', '0002_application_is_applied'),
        ('student', '0008_auto_20210121_1116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentDocument',
            new_name='Document',
        ),
    ]