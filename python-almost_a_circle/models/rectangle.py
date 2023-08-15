"""This module contains the Rectangle class, which represents a rectangle object."""

from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The horizontal position of the rectangle.
        y (int): The vertical position of the rectangle.
        id (int): The unique identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Constructor method for Rectangle class.
        area(self): Returns the area of the rectangle.
        display(self): Prints the rectangle using '#' symbol.
        __str__(self): Returns a string representation of the Rectangle instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal position of the rectangle. Default is 0.
            y (int): The vertical position of the rectangle. Default is 0.
            id (int, optional): The unique identifier for the rectangle.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If width is <= 0.

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If height is <= 0.

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """int: The horizontal position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal position of the rectangle.

        Args:
            value (int): The new horizontal position value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If x is < 0.

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """int: The vertical position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical position of the rectangle.

        Args:
            value (int): The new vertical position value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If y is < 0.

        Returns:
            None
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
    
    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.width * self.height

    def display(self):
        """Prints the rectangle using '#' symbol.

        Returns:
            None
        """

        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the Rectangle instance.

        Returns:
            str: A string representation of the object.
        """

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"