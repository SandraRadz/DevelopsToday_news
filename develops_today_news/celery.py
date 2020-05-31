import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'develops_today_news.settings')

app = Celery('develops_today_news')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'news.tasks.reset_upvotes',
        'schedule': crontab(minute=0, hour=0)
    },
}