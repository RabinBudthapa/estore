# Generated by Django 5.0.6 on 2024-07-12 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_remove_orderitem_image_remove_orderitem_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="home.product"
            ),
        ),
    ]
