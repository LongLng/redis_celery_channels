import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','realtime.settings')


app = Celery('realtime')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule = {
	'get_joke_3s':{
		'task':'app.tasks.get_joke',
		'schedule':3.0
	}
}
app.autodiscover_tasks()