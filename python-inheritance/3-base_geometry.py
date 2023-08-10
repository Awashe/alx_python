"""This is an empty class BaseGeometry."""
class BaseGeometry:
    """
    A base class for geometrical objects.
    """
    def __dir__(self):
        return list(self.__dict__.keys())
