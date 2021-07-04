from rest_framework.serializers import ModelSerializer
from news.models.category import Category


class CategoryListSZ(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
