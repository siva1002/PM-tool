import os

from celery import Celery
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
app = Celery('myproject')
app.conf.broker_url = os.environ.get("CELERY_URL")
app.config_from_object("django.conf:settings")
# app.conf.result_backend =f'db+sqlite:///{os.path.join(BASE_DIR, "scheduler.sqlite3")}'
app.autodiscover_tasks(settings.INSTALLED_APPS)