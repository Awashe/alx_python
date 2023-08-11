"""Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py)."""

class BaseGeometry:
    """
    A class representing basic geometry operations

    ...

    Methods
    -------
    area(self):
        Raises an Exception indicating that the method is not yet implemented.
    integer_validator(self, name, value):
        Validates that the given value is an integer greater than 0.

    """

    def area(self):
        """
        Raises an Exception indicating that the method is not yet implemented.

        Parameters:
        None

        Returns:
        None

        Raises:
        Exception: indicating that the method is not yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the given value is an integer greater than 0.

        Parameters:
        name (str): The name of the variable being validated.
        value (int): The value to validate.

        Returns:
        None

        Raises:
        TypeError: if the value is not an integer.
        ValueError: if the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    
class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle shape

    ...

    Attributes
    ----------
    __width : int
        The width of the Rectangle object.
    __height : int
        The height of the Rectangle object.

    Methods
    -------
    area(self):
        Returns the area of the Rectangle object.
    __str__(self):
        Returns a string representation of the Rectangle object.
    """

    def __init__(self, width, height):
        """
        Constructs and initializes a new Rectangle object with the
        specified width and height values.

        Parameters:
        width (int): The width of the Rectangle object.
        height (int): The height of the Rectangle object.

        Returns:
        None

        Raises:
        TypeError: if either width or height is not an integer.
        ValueError: if either width or height is less than or equal to 0.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the Rectangle object.

        Parameters:
        None

        Returns:
        The area of the Rectangle object.

        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Parameters:
        None

        Returns:
        A string representation of the Rectangle object.

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)