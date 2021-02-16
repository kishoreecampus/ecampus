# Generated by Django 3.1.5 on 2021-01-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createclass',
            name='created_by',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='createclass',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='createclassgroup',
            name='created_by',
            field=models.CharField(default=None, max_length=60, verbose_name='created_by'),
        ),
        migrations.AddField(
            model_name='createclassgroup',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='createsection',
            name='created_by',
            field=models.CharField(default=None, max_length=60, verbose_name='created_by'),
        ),
        migrations.AddField(
            model_name='createsection',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
