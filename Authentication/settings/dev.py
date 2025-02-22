from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-akbtxz(i#3k6=2f@notw50cr92g#xp81*zg%-g41j!7#3401j@'

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "auths.CusUser"

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
