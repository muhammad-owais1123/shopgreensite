# Generated by Django 5.0.7 on 2024-08-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0020_productinfo_inventory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productinfo",
            name="inventory",
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
