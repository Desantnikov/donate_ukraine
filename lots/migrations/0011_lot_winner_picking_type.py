# Generated by Django 3.2.10 on 2023-03-18 17:49

from django.db import migrations, models

import lots.constants


class Migration(migrations.Migration):
    dependencies = [
        ("lots", "0010_alter_lot_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="lot",
            name="winner_picking_type",
            field=models.CharField(
                choices=[("TOP_DONATER", "TOP_DONATER"), ("RANDOM_DONATER", "RANDOM_DONATER")],
                default=lots.constants.WINNER_PICKING_TYPE["TOP_DONATER"],
                max_length=50,
            ),
        ),
    ]
