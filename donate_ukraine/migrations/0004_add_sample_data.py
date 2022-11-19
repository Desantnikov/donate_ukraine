# Generated by Django 2.2.26 on 2022-01-11 15:07

from django.db import migrations


def forward(apps, schema_editor) -> None:
    User = apps.get_model("donate_ukraine", "User")
    Lot = apps.get_model("donate_ukraine", "Lot")

    user = User(email="admin@gmail.com")

    lot = Lot(
        creator=user,
        description="sample description",
        requisites=["card number", "second card number"],
    )

    user.save()
    lot.save()


class Migration(migrations.Migration):

    dependencies = [
        ("donate_ukraine", "0003_alter_lot_requisites"),
    ]

    operations = [migrations.RunPython(forward, migrations.RunPython.noop)]