import os
from .base import *
from django.core.management.utils import get_random_secret_key


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY", default=get_random_secret_key)

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "auths.CustomUser"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIR = [BASE_DIR / "static/"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'

STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

LOGIN_URL = "login"
