# Generated by Django 4.2.4 on 2023-10-10 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_county',
        ),
    ]