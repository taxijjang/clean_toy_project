from domains.repositories import StoryReader
from domains.objects import Story as D_Story
from .models import Story
from news.serializers.story_sz import StoryListSZ

class StoryReader(StoryReader):
    def read(self, flat_form, category):
        serializer = StoryListSZ(Story.objects.get(flat_form=flat_form, category=category))
        return D_Story(**serializer.validated_data)