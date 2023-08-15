"""This module contains the square object class, which represents a square object."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square.

    Attributes:
        size (int): The size of the square.
        x (int): The horizontal position of the square.
        y (int): The vertical position of the square.
        id (int): The unique identifier for the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor method for Square class.
        __str__(self): Returns a string representation of the Square instance.
        update(self, *args, **kwargs): Update the attributes of the object.
        area(self): Returns the area of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for Square class.

        Args:
            size (int): The size of the square.
            x (int): The horizontal position of the square. Default is 0.
            y (int): The vertical position of the square. Default is 0.
            id (int, optional): The unique identifier for the square.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If size is <= 0.

        Returns:
            None
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance.

        Returns:
            str: A string representation of the object.
        """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the attributes of the object.

        Args:
            *args: List of arguments that corresponds to class attributes.
            **kwargs: Dictionary of key-value pairs that corresponds to class attributes.

        Returns:
            None
        """
        arg_names = ['id', 'size', 'x', 'y']
        num_args = len(args)

        for i, value in enumerate(args):
            if i >= num_args:
                break
            setattr(self, arg_names[i], value)

        if not args or num_args < 4:
            for key, value in kwargs.items():
                setattr(self, key, value)

        self.height = self.width = self.size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.width ** 2