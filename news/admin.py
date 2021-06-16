from django.contrib import admin

from news.models.flatform import FlatForm
from news.models.category import Category
from news.models.story import Story


@admin.register(FlatForm)
class FlatFormAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'url')
    ordering = ['-pk']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'flatform', 'url')
    ordering = ['-pk']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'category')
    ordering = ['-pk']