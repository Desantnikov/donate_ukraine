from django.db import migrations
from django.conf import settings


def add_dev_superuser(apps, schema_editor):
    if not settings.IS_HEROKU:
        print("Not heroku env, adding superuser")
        User = apps.get_model("users", "User")
        User.objects.create_superuser(username="local", password="12345678", email="local@local.com")
        return
    print("Heroky env, skip adding superuser")


class Migration(migrations.Migration):

    dependencies = [("users", "0003_alter_user_email")]

    operations = [migrations.RunPython(add_dev_superuser, migrations.RunPython.noop)]
