import os
from celery import Celery

from startup_tasks.tasks import get_trade_stream_data

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


get_trade_stream_data.delay()