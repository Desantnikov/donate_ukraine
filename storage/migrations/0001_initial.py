# Generated by Django 4.1.4 on 2022-12-07 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("donate_ukraine", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LotImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default=None, max_length=50)),
                ("img", models.ImageField(default=None, upload_to="images/")),
                ("lot", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="donate_ukraine.lot")),
            ],
        ),
    ]
