# Generated by Django 5.0.7 on 2024-08-24 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0036_alter_orderdetails_orderitems"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderdetails",
            name="orderItems",
        ),
    ]
