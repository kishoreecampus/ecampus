# Generated by Django 3.1.4 on 2021-01-20 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('preadmission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_photo', models.ImageField(height_field=300, upload_to='uploads/', verbose_name='Photo', width_field=300)),
                ('birth_certificate', models.ImageField(upload_to='uploads/', verbose_name='Photo')),
                ('tc', models.ImageField(null=True, upload_to='uploads/', verbose_name='Photo')),
                ('other_document', models.ImageField(null=True, upload_to='uploads/', verbose_name='Photo')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded On')),
                ('application_number', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='preadmission.application')),
                ('student_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='student.student')),
            ],
        ),
    ]
