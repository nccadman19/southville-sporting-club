# Generated by Django 4.2.4 on 2023-11-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_original_bag_order_stripe_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='product_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
