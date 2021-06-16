from django.db import models
from news.models.base import BaseModel


class Story(BaseModel):
    title = models.CharField(max_length=20)
    rank = models.IntegerField(default=1)
    content = models.CharField(max_length=1000)
    url = models.CharField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='stories')

    def __str__(self):
        return self.title
