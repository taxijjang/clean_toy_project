class NullOrNegativePriceException(Exception):
    pass


class NullOrNegativeParityException(Exception):
    pass


class InvalidReference(Exception):
    pass


class TooManyProductsRemoved(Exception):
    pass


class Category:
    """
    here is the buisness logic of cateogry entity
    """

    def __init__(self):
        self._title = None
        self._flat_form = None
        self._url = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def flat_form(self):
        return self._flat_form

    @flat_form.setter
    def flat_form(self, flat_form):
        self._flat_form = flat_form

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url