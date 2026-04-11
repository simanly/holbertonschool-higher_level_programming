#!/usr/bin/python3
"""
Module for Shape, Circle, Rectangle and duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for a shape."""
    @abstractmethod
    def area(self):
        """Method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class."""
    def __init__(self, radius):
        """Initialize with radius."""
        self.radius = radius

    def area(self):
        """Return circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width, height):
        """Initialize with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function to print shape info using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
