from urllib.parse import urlparse

from .settings import *


db_url = os.getenv("DATABASE_URL")
db_url_obj = urlparse(db_url)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": db_url_obj.username,
        "PASSWORD": db_url_obj.password,
        "NAME": db_url_obj.path.lstrip("/"),
        "HOST": db_url_obj.hostname,
    }
}
