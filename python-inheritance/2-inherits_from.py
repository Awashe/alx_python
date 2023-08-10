""" This function returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""
def inherit_from(obj, a_class):
    """
    Determine if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    obj: An object of any type.
    a_class: A class object.

    Returns:
    True if the object is an instance of a subclass (directly or indirectly)
    of the specified class, else False.
    """
    return issubclass(obj, a_class)