from rest_framework.serializers import ModelSerializer
from news.models.story import Story


class StoryListSZ(ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'rank', 'url',)
