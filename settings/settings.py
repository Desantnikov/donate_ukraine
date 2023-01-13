import os
from datetime import timedelta
from pathlib import Path


# `compose` means app was launched by `docker-compose up`
# `regular` means app was launched outside of container (by pycharm button or regular `manage.py runserver`)
LAUNCH_MODE = os.getenv("LAUNCH_MODE", "compose").lower()

IS_COMPOSE = LAUNCH_MODE == "compose"
IS_REGULAR = LAUNCH_MODE == "regular"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-04_7wq%!3o4p9+5he^^v#_ddgc4wh08xc9zb0@hk_hooq$=gx_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "pytest_django",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "drf_yasg",
    "guardian",
    "users",
    "donate_ukraine",
    "storage",
    "monobank",
    "mixins",
]


SITE_ID = 1
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db" if IS_COMPOSE else "172.18.0.2",
        "PORT": "5432",
    },
}

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSIONS_CLASSES': [
    #     "rest_framework.permissions.IsAuthenticated",
    #     "rest_framework.permissions.DjangoObjectPermissions",
    # ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",
]

ACCOUNT_AUTHENTICATION_METHOD = "username"

ACCOUNT_CONFIRM_EMAIL_ON_GET = False

PASSWORD_MIN_LENGTH = 1


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CORS_ALLOW_ALL_ORIGINS = True

APPEND_SLASH = True

SIMPLE_JWT = {
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
}

MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

AUTH_USER_MODEL = "users.User"
CUSTOM_USER_MODEL = "users.User"
