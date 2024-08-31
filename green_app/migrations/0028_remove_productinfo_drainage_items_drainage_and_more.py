# Generated by Django 5.0.7 on 2024-08-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0027_remove_items_drainage_remove_items_gloss_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productinfo",
            name="drainage",
        ),
        migrations.AddField(
            model_name="items",
            name="drainage",
            field=models.CharField(
                choices=[("Yes", "yes"), ("No", "no")], max_length=3, null=True
            ),
        ),
        migrations.AddField(
            model_name="items",
            name="gloss",
            field=models.CharField(
                choices=[("High", "high"), ("Low", "low")], max_length=20, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="drainage",
            field=models.CharField(
                choices=[("Yes", "yes"), ("No", "no")], max_length=3, null=True
            ),
        ),
    ]
