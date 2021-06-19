import requests

from celery import shared_task
from bs4 import BeautifulSoup

from django.db import transaction
from news.models.flatform import FlatForm
from news.models.story import Story


@shared_task
def crawlings():
    news_list = []
    for flatform in FlatForm.objects.all():
        print(flatform)
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