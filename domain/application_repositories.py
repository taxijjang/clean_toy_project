from abc import ABC, abstractmethod


class InterfaceStoryReader(ABC):
    @abstractmethod
    def read(self, flat_form, category):
        raise NotImplementedError()


class InterfaceStoryWriter(ABC):
    @abstractmethod
    def write(self, obj):
        raise NotImplementedError()
