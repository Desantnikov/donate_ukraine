# Generated by Django 3.2.10 on 2023-03-18 02:22

from django.db import migrations, models

import lots.constants


class Migration(migrations.Migration):

    dependencies = [
        ("lots", "0009_alter_lot_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lot",
            name="status",
            field=models.CharField(
                choices=[("MODERATION", "MODERATION"), ("ACTIVE", "ACTIVE"), ("CLOSED", "CLOSED")],
                default=lots.constants.LOT_STATUS["MODERATION"],
                max_length=50,
            ),
        ),
    ]
