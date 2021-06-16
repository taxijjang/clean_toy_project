from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clean_toy_project.settings')

app = Celery('clean_toy_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

#등록된 장고 앱 설정에서 task를 불러옵니다.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))