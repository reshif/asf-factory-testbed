SECRET_KEY = "dev-only-not-a-secret"
DEBUG = True
INSTALLED_APPS = ["django.contrib.contenttypes", "shop"]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
