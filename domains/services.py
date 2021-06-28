from .repositories import StoryReader
from .objects import Story

class StoryService:

    def __init__(self, reader, data):
        self._reader = reader
        self._data = data

    def execute(self):
        pass