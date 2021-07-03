from domain.application_repositories import InterfaceStoryReader
from domain.application_repositories import InterfaceStoryWriter
from domain.entity import Story as D_Story
from .models import Story
from news.serializers.story_sz import StoryListSZ


class StoryReader(InterfaceStoryReader):
    def read(self, flat_form, category):
        serializer = StoryListSZ(Story.objects.get(flat_form=flat_form, category=category))
        return D_Story(**serializer.validated_data)


class StoryWriter(InterfaceStoryWriter):
    def write(self, obj):
        story = Story(
            title=obj.title,
            rank=obj.rank,
            url=obj.url,
            flat_form=obj.flat_form,
            category=obj.category
        )
        story.save()

        return story
