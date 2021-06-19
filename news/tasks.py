import requests

from celery import shared_task
from bs4 import BeautifulSoup

from django.db import transaction
from news.models.flatform import FlatForm
from news.models.category import Category
from news.models.story import Story


@shared_task
def crawlings():
    news_list = []
    for flatform in FlatForm.objects.all():
        for category in flatform.categories.all():
            request = requests.get(category.full_url)
            soup = BeautifulSoup(request.text, 'html.parser')

            news = soup.select(flatform.select_location)

            if not news:
                break

            titles = news[0].find_all('a', class_=flatform.a_tag_class_name)

            for rank, title in enumerate(titles):
                story = Story(
                    flat_form=flatform,
                    category=category,
                    rank=rank + 1,
                    title=title.text,
                    url=flatform.url[:-1] + title.get('href') if flatform.title == 'naver' else title.get('href')
                )
                news_list.append(story)
    update_news(news_list)


@transaction.atomic
def update_news(news_list):
    Story.truncate()
    Story.objects.bulk_create(news_list)

def abc():
    s = '''Django	3.1	3.2.4
amqp	5.0.6	5.0.6
anyjson	0.3.3	0.3.3
asgiref	3.2.10	3.3.4
beautifulsoup4	4.9.3	4.9.3
billiard	3.6.4.0	3.6.4.0
bs4	0.0.1	0.0.1
cached-property	1.5.2	1.5.2
celery	5.1.0	5.1.1
certifi	2021.5.30	2021.5.30
chardet	4.0.0	4.0.0
click	7.1.2	8.0.1
click-didyoumean	0.0.3	0.0.3
click-plugins	1.1.1	1.1.1
click-repl	0.2.0	0.2.0
django-celery-beat	2.2.0	2.2.0
django-celery-results	2.0.1	2.1.0
django-timezone-field	4.1.2	4.1.2
djangorestframework	3.12.4	3.12.4
drf-writable-nested	0.6.3	0.6.3
idna	2.10	3.2
importlib-metadata	4.5.0	4.5.0
kombu	5.1.0	5.1.0
mysqlclient	2.0.3	2.0.3
pip	21.1.2	21.1.2
prompt-toolkit	3.0.18	3.0.19
python-crontab	2.5.1	2.5.1
python-dateutil	2.8.1	2.8.1
pytz	2021.1	2021.1
requests	2.25.1	2.25.1
setuptools	40.6.2	57.0.0
six	1.16.0	1.16.0
soupsieve	2.2.1	2.2.1
sqlparse	0.4.1	0.4.1
transaction	3.0.1	3.0.1
typing-extensions	3.10.0.0	3.10.0.0
urllib3	1.26.5	1.26.5
vine	5.0.0	5.0.0
wcwidth	0.2.5	0.2.5
wheel	0.36.2	0.36.2
zipp	3.4.1	3.4.1
zope.interface	5.4.0	5.4.0'''
    ss = s.replace('	','==')
    sss = ss.split('\n')

    result = ''
    for ssss in sss:
        result += ssss[:ssss.rfind('==')]+'\n'

    print(result)