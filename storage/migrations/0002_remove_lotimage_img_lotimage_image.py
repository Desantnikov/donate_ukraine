# Generated by Django 4.1.4 on 2022-12-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lotimage",
            name="img",
        ),
        migrations.AddField(
            model_name="lotimage",
            name="image",
            field=models.ImageField(default=None, upload_to="media/images/lots"),
        ),
    ]
