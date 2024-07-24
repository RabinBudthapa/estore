# Generated by Django 5.0.6 on 2024-06-09 14:33

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="name",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="name",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="name",
                unique=True,
            ),
        ),
    ]
