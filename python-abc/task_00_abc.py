#!/usr/bin/python3
"""
This module contains an abstract class Animal and its subclasses Dog and Cat.
It demonstrates the use of Abstract Base Classes (ABCs).
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method sound that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Subclass Dog that inherits from Animal."""

    def sound(self):
        """Returns the sound of a Dog."""
        return "Bark"


class Cat(Animal):
    """Subclass Cat that inherits from Animal."""

    def sound(self):
        """Returns the sound of a Cat."""
        return "Meow"
