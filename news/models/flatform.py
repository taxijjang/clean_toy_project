from django.db import models
from news.models.base import BaseModel


class FlatForm(BaseModel):
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    select_location = models.CharField(max_length=500)
    a_tag_class_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title