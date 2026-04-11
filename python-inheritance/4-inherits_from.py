#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
