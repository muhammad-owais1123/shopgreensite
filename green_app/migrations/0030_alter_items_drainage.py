# Generated by Django 5.0.7 on 2024-08-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0029_alter_items_drainage_alter_product_drainage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="drainage",
            field=models.CharField(
                choices=[("Yes", "yes"), ("No", "no")], max_length=3, null=True
            ),
        ),
    ]
