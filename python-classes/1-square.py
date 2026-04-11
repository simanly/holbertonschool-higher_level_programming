#!/usr/bin/python3
"""
This module defines a Square class.
It focuses on the initialization of the private attribute size.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size):
        """
        Initializes the square with a size.

        Args:
            size (int): The length of a side of the square.
        """
        self.__size = size
