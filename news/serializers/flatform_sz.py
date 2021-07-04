from rest_framework.serializers import ModelSerializer
from news.models.flatform import FlatForm


class FlatformListSZ(ModelSerializer):
    class Meta:
        model = FlatForm
        fields = ('id', 'title')
