from .base import *
import os
from django.core.management.utils import get_random_secret_key


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEBUG = os.environ.get("DEBUG", "False")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DEPLOY_SECRET_KEY", default=get_random_secret_key)


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1").split(",")

AUTH_USER_MODEL = "auths.CusUser"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}


STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIR = [BASE_DIR / "static/"]

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "uploads"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}   # dont forget to add whitenoise middleware for the using whitenoise in deployment

LOGIN_URL = "login"
