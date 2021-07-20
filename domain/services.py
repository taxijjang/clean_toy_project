from domain.application_repositories import InterfaceStoryReader, InterfaceStoryWriter
from domain.entity import Story


class StoryService:

    def __init__(self, reader: InterfaceStoryReader, writer: InterfaceStoryWriter, data):
        self._reader = reader
        self._writer = writer
        self._data = data

    def execute(self):
        story = self._data
        result = self._writer.write(story)
        return {
            'id': result.id,
            'title': result.title,
            'url': result.url,
            'flat_form': result.flat_form.title,
            'category': result.category.title,
        }
