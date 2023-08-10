""" This function returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""
def inherit_from(obj, a_class):
    """
    Determines if it is subclass.
    """
    return issubclass(obj, a_class)