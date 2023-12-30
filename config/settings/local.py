import os

import environ

from config.settings.base import *

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(".env")

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]

DEBUG = env("DEBUG")

SQLITE_DB_PATH = os.path.join(BASE_DIR, env("SQLITE_URL"))
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": SQLITE_DB_PATH,
    }
}
