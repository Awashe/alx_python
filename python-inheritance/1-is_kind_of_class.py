"""This function returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False."""
def is_kind_of_class(obj, a_class):
    """
        Determine if an object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
    obj: An object of any type.
    a_class: A class object.

    Returns:
    True if the object is an instance of the specified class or
    inherited from the specified class, else False.
    """
    return isinstance(obj, a_class)