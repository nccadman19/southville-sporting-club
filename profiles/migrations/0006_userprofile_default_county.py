# Generated by Django 4.2.4 on 2023-11-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_default_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
