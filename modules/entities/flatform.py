class NullOrNegativePriceException(Exception):
    pass


class NullOrNegativeParityException(Exception):
    pass


class InvalidReference(Exception):
    pass


class TooManyProductsRemoved(Exception):
    pass


class FlatForm:
    """
    here is the buisness logic of flatform entity
    """

    def __init__(self, title, url, select_location, a_tag_class_name):
        self.title = title
        self.url = url
        self.select_location = select_location
        self.a_tag_class_name = a_tag_class_name
