#!/usr/bin/python3
"""
This module defines a Square class that can print itself.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The current size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the current square area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
