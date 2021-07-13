import requests

from celery import shared_task
from bs4 import BeautifulSoup

from domain.services import StoryService
from domain.repositories import StoryReader
from domain.repositories import StoryWriter
from news.models.flatform import FlatForm
from news.models.story import Story


@shared_task
def crawlings():
    Story.truncate()
    for flatform in FlatForm.objects.all():
        for category in flatform.categories.all():
            request = requests.get(category.full_url)
            soup = BeautifulSoup(request.text, 'html.parser')

            news = soup.select(flatform.select_location)

            if not news:
                break

            titles = news[0].find_all('a', class_=flatform.a_tag_class_name)

            for rank, title in enumerate(titles):
                data = dict(
                    flat_form=flatform,
                    category=category,
                    rank=rank + 1,
                    title=title.text,
                    url=flatform.url[:-1] + title.get('href') if flatform.title == 'naver' else title.get('href')
                ) # data class 로 저장
                story_service = StoryService(
                    reader=StoryReader(),
                    writer=StoryWriter(),
                    data=data
                )

                story_service.execute()
