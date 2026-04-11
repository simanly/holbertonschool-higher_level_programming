#!/usr/bin/python3
"""
This module demonstrates the use of Mixins by creating a Dragon class
that can swim and fly, along with its own unique behavior.
"""


class SwimMixin:
    """Mixin that provides swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits capabilities from SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints a roaring message unique to the dragon."""
        print("The dragon roars!")
