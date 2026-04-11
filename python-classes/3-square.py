#!/usr/bin/python3
"""
This module defines a Square class with size validation and area calculation.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
