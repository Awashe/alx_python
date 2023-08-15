"""This module contains the Base class, which is the foundation for all other classes in this project."""

class Base:
    """This is the base class for all other classes in the project. It manages the id attribute for all instances and
    helps avoid duplicating the same code in multiple classes.

    Attributes:
        __nb_objects (int): A private class attribute that counts the number of objects created and is used to assign
            a unique id to each instance.

        id (int): A public instance attribute representing the unique identifier for each instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for Base class.

        Args:
            id (int, optional): The unique identifier for the instance. If not provided, it is automatically generated.

        Returns:
            None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects