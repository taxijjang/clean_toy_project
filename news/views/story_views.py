from rest_framework.generics import ListAPIView
from rest_framework import exceptions
from news.models.flatform import FlatForm
from news.models.category import Category
from news.models.story import Story

from news.serializers.story_sz import StoryListSZ


class StoryListView(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryListSZ

    def get_queryset(self):
        flat_form_title = self.kwargs.get('flatform')
        category_title = self.kwargs.get('category')

        if not FlatForm.objects.filter(title=flat_form_title):
            raise exceptions.NotFound(detail='flatform not exists')

        if not Category.objects.filter(title=category_title):
            raise exceptions.NotFound(detail='category not exists')

        return self.queryset.filter(flat_form__title=flat_form_title, category__title=category_title)
