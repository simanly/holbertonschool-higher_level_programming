#!/usr/bin/python3
"""
This module provides a function that looks up all available attributes
and methods of a given object. It is part of the inheritance project.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the object's attributes.
    """
    return dir(obj)
