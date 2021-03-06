from domain.application_repositories import InterfaceStoryReader
from domain.application_repositories import InterfaceStoryWriter
from domain.entity import Story as D_Story
from news.models import Story, Category, FlatForm
from news.serializers.story_sz import StoryListSZ


class StoryReader(InterfaceStoryReader):
    def read(self, flat_form, category):
        serializer = StoryListSZ(Story.objects.get(flat_form=flat_form, category=category))
        return D_Story(**serializer.validated_data)


class StoryWriter(InterfaceStoryWriter):
    def write(self, story):
        new_story = Story(
            rank=story.rank,
            title=story.title,
            url=story.url,
            category=Category.objects.get(id=story.category),
            flat_form=FlatForm.objects.get(id=story.flat_form)
        )
        new_story.save()