# Generated by Django 3.2.10 on 2023-02-23 14:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lots", "0003_auto_20230210_1135"),
    ]

    operations = [
        migrations.AddField(
            model_name="lot",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
