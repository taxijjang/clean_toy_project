from abc import ABC, abstractmethod

from .objects import Story

class StoryReader(ABC):
    @abstractmethod
    def read(self, flat_form, category ) -> Story:
        raise NotImplementedError()