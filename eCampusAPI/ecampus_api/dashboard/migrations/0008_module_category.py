# Generated by Django 3.1.4 on 2021-01-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210105_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='category',
            field=models.CharField(default=None, max_length=30, verbose_name='Category'),
        ),
    ]