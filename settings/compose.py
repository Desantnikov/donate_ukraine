from settings.heroku import *


IS_HEROKU = False


SECRET_KEY = "django-insecure-04_7wq%!3o4p9+5he^^v#_ddgc4wh08xc9zb0@hk_hooq$=gx_"

DEBUG = True
ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": "5432",
    },
}
