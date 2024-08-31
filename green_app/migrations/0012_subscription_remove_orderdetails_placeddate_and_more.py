# Generated by Django 5.0.7 on 2024-08-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("green_app", "0011_alter_reviews_ratings"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="orderdetails",
            name="placedDate",
        ),
        migrations.RemoveField(
            model_name="orderdetails",
            name="placedTime",
        ),
    ]
