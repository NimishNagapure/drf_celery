from __future__ import absolute_import, unicode_literals
from gettext import bind_textdomain_codeset
import os
from celery import Celery
from django.conf import settings
from pytz import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_celery.settings')

app = Celery('dj_celery')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {}

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r} timezone: {app.conf.timezone}')