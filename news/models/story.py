from django.db import models
from django.db import connection
from news.models.base import BaseModel


class Story(BaseModel):
    title = models.CharField(max_length=1000)
    rank = models.IntegerField(default=1)
    url = models.CharField(max_length=500)
    flatform = models.ForeignKey('FlatForm', on_delete=models.SET_NULL, null=True, related_name='stories')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='stories')

    def __str__(self):
        return self.title

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE {cls._meta.db_table}")
