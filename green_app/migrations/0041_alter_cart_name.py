# Generated by Django 5.0.7 on 2024-08-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0040_alter_cart_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]