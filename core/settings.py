from pathlib import Path
import os
import json


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG = json.loads(open(str(BASE_DIR) + "/config.json", "r").read())

SECRET_KEY = CONFIG["SECRET_KEY"]


DEBUG = CONFIG["DEBUG"]

ALLOWED_HOSTS = CONFIG["ALLOWED_HOSTS"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


INSTALLED_APPS += [
    "auth",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"


if CONFIG["DATABASE"] == "pro":
    DATABASES = {
        "default": {
            "ENGINE": CONFIG["DB_ENGINE"],
            "NAME": CONFIG["DB_NAME"],
            "USER": CONFIG["DB_USER"],
            "PASSWORD": CONFIG["DB_PASSWORD"],
            "HOST": CONFIG["DB_HOST"],
            "PORT": CONFIG["DB_PORT"],
            #     'OPTIONS': {
            #         'keepalives': 1,
            #         'keepalives_idle': 30,
            #         'keepalives_interval': 10,
            #         'keepalives_count': 5,
            #         'connect_timeout': 10,
            #         'client_encoding': 'UTF8',
            #     },
            # 'CONN_MAX_AGE': 300,
            # 'ATOMIC_REQUESTS': False,
            # 'AUTOCOMMIT': True,
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Karachi"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
