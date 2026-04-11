#!/usr/bin/python3
"""
Module for multiple inheritance exploration with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints fish swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat message."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints bird flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Overrides fly with flying fish specific message."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides swim with flying fish specific message."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat with flying fish specific message."""
        print("The flying fish lives both in water and the sky!")
