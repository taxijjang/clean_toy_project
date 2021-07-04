from django.db import models
from news.models.base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=20)
    flat_form = models.ForeignKey('FlatForm', on_delete=models.SET_NULL, null=True, related_name='categories')
    url = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    @property
    def full_url(self):
        return ''.join([self.flat_form.url, self.url])