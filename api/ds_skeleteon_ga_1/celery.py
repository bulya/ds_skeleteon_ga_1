import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ds_skeleteon_ga_1.settings")

celery_app = Celery("ds_skeleteon_ga_1")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()
