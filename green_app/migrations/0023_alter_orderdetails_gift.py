# Generated by Django 5.0.7 on 2024-08-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0022_alter_orderdetails_gift"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetails",
            name="gift",
            field=models.CharField(
                choices=[("Yes", "yes"), ("No", "no")], max_length=20
            ),
        ),
    ]
