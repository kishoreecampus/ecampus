# Generated by Django 3.1.5 on 2021-01-27 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20210126_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='mobil_number',
            new_name='mobile_number',
        ),
    ]
