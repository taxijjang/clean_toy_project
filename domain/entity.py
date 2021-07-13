from dataclasses import dataclass


@dataclass
class Story:
    def __init__(self, title, rank, url, flat_form, category, id=None):
        self._id = id
        self._title = title
        self._rank = rank
        self._url = url
        self._flat_form = flat_form
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def rank(self):
        return self._rank

    @property
    def url(self):
        return self._url

    @property
    def flat_form(self):
        return self._flat_form

    @property
    def category(self):
        return self._category
