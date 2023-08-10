def is_same_class(obj, a_class):
    """
    determines if an object is exactly instance of specified class.

    Ags:
    obj: an object of any type.
    a_class: A class object.

    Returns:
    True if the object is exactly an instance of the specified class, 
    else false.
    """
    return type(obj) is a_class