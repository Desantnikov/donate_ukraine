# Generated by Django 4.1.5 on 2023-01-13 02:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MonobankJar",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(default="", max_length=40)),
                ("monobank_id", models.CharField(max_length=40, null=True)),
                ("link", models.URLField(default="", max_length=40)),
                ("current_balance", models.IntegerField(default=0)),
                ("goal", models.IntegerField(default=0)),
                ("highest_bid", models.IntegerField(default=0)),
                ("last_updated", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
