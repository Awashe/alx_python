"""This module contains the square object class, which represents a square object."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square.

    Inherits:
        Rectangle: The parent class for square.

    Attributes:
        size (int): The size (width/height) of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor method for Square class.
        __str__(self): Returns a string representation of the Square instance.
        update(self, *args, **kwargs): Updates the attributes of the square instance based on the arguments.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for Square class.

        Args:
            size (int): The size (width/height) of the square.
            x (int): The horizontal position of the square. Default is 0.
            y (int): The vertical position of the square. Default is 0.
            id (int, optional): The unique identifier for the square.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size (width/height) of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            ValueError: If size is <= 0.

        Returns:
            None
        """

        if value <= 0:
            raise ValueError("size must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """Return a string representation of the Square instance.

        Returns:
            str: A string representation of the object.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the attributes of the square instance based on the arguments.

        Args:
            *args: A tuple of arguments.
            **kwargs: A dictionary of key-value arguments.

        Returns:
            None
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, val in zip(attrs, args):
                setattr(self, attr, val)
        elif kwargs:
            for attr, val in kwargs.items():
                setattr(self, attr, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance.

        Returns:
            dict: A dictionary representation of the object.
        """

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}