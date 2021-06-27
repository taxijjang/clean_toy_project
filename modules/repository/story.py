from news.models import Story as StoryORM
from ..entities.story import Story

class EntityDoesNotExist(Exception):
    pass

class StoryDBRepository:
    def get_find_by_flat_form_and_category(self, flat_form, category):
        try:
            orm_story = StoryORM.objects.get(flat_form=flat_form, category=category)
        except StoryORM.DoesNotExist as e:
            raise EntityDoesNotExist
        return self.

    def decode_orm_stories(self, orm_story_queryset):
        story_list = []

        for orm_story in orm_story_queryset:
            story = Story()
            story_entity = story.set_params(

            )
