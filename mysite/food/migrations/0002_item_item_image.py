# Generated by Django 4.2.7 on 2023-12-08 01:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="item_image",
            field=models.CharField(
                default="https://images.pexels.com/photos/7495206/pexels-photo-7495206.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load",
                max_length=5000,
            ),
        ),
    ]
