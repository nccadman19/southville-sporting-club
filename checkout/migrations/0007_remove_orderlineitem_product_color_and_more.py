# Generated by Django 4.2.4 on 2023-11-07 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_orderlineitem_product_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_color',
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
