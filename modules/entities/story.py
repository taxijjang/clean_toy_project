class NullOrNegativePriceException(Exception):
    pass


class NullOrNegativeParityException(Exception):
    pass


class InvalidReference(Exception):
    pass


class TooManyProductsRemoved(Exception):
    pass


class Story:
    """
    here is the buisness logic of story entity
    """

    def __init__(self):
        self._title = None
        self._rank = None
        self._url = None
        self._flat_form = None
        self._category = None

    def set_params(self, title, rank, url, flat_form, category):
        self._title = title
        self._rank = rank
        self._url = url
        self._flat_form = flat_form
        self._category = category

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
        return self._cateogry