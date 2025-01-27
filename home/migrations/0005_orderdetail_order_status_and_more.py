# Generated by Django 5.0.6 on 2024-07-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderdetail",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("Order Received", "Order Received"),
                    ("Order Processing", "Order Processing"),
                    ("On the way", "On the way"),
                    ("Order Completed", "Order Completed"),
                    ("Order Canceled", "Order Canceled"),
                ],
                default="Order Processing",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="payment_completed",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name="orderdetail",
            name="total",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="orderdetail",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Khalti", "Khalti"),
                    ("Cash On Delivery", "Cash On Delivery"),
                ],
                default="Cash On Delivery",
                max_length=20,
            ),
        ),
    ]
