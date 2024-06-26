# Generated by Django 3.2.10 on 2023-02-10 11:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lots", "0002_auto_20230124_1028"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lot",
            name="report_images",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.ImageField(upload_to="static"), blank=True, default=list, size=None
            ),
        ),
        migrations.AlterField(
            model_name="lot",
            name="report_text",
            field=models.CharField(blank=True, default="", max_length=512),
        ),
    ]
