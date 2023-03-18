# Generated by Django 3.2.10 on 2023-03-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lots", "0005_lot_statuses"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lot",
            options={
                "default_permissions": ("add", "change", "delete"),
                "get_latest_by": "-created_at",
                "ordering": ("-created_at",),
                "permissions": (("view_post", "Can view post"),),
            },
        ),
        migrations.AddField(
            model_name="lot",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
