# Generated by Django 5.0.6 on 2024-07-12 14:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0010_remove_cart_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderitem",
            name="image",
        ),
        migrations.RemoveField(
            model_name="orderitem",
            name="total",
        ),
    ]
