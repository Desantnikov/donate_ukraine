# Generated by Django 4.1.4 on 2023-01-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donate_ukraine", "0005_alter_user_api_token"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lot",
            name="requisites",
        ),
        migrations.AddField(
            model_name="lot",
            name="is_under_moderation",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default="", max_length=20),
        ),
    ]
