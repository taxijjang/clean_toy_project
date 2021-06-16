import requests

from celery import shared_task
from bs4 import BeautifulSoup

from news.models.flatform import FlatForm
from news.models.category import Category
from news.models.story import Story


@shared_task
def add(x, y):
    return x + y



def crawlings():
    for flatform in FlatForm.objects.all():
        if flatform.title == 'naver':
            continue
        news_list = []
        for category in flatform.categories.all():
            request = requests.get(category.full_url)
            soup = BeautifulSoup(request.text, 'html.parser')

            news = soup.select(flatform.select_location)
            titles = news[0].find_all('a', class_=flatform.a_tag_class_name)

            for rank, title in enumerate(titles):
                news_data = dict(
                    rank=rank+1,
                    title=title.text,
                    url=flatform.url + title.get('href') if flatform.title == 'naver' else title.get('href')
                )
                news_list.append(news_data)

                print(flatform.title, category.title, news_data)
        print(news_list)