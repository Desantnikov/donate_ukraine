# Generated by Django 4.1.4 on 2022-12-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0004_alter_lotimage_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lotimage",
            name="file",
            field=models.ImageField(default=None, upload_to="media/images/lots"),
        ),
    ]
