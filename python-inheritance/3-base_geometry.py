"""This is an empty class BaseGeometry."""
class BaseGeometry:
    """
    A base class for geometrical objects.
    """

    def __init__(self):
        pass

    def __dir__(self):
        return list(self.__dict__.keys()) + \
               [attr for attr in dir(type(self)) if not attr.startswith("__")]

    def __repr__(self):
        return "<{} object at {}>".format(type(self).__name__, hex(id(self)))
