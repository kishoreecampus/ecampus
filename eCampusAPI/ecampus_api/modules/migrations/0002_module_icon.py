# Generated by Django 3.1.4 on 2021-01-17 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='icon',
            field=models.URLField(max_length=250, null=True, verbose_name='Icon Path'),
        ),
    ]
