# Generated by Django 4.2.4 on 2023-09-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
