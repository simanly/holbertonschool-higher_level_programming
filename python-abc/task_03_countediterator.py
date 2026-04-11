#!/usr/bin/python3
"""
This module defines the CountedIterator class that extends a standard iterator.
It keeps track of the number of items that have been iterated over.
"""


class CountedIterator:
    """A class that wraps an iterator and counts its iterations."""

    def __init__(self, data):
        """
        Initializes the CountedIterator.
        Args:
            data (iterable): The data to be iterated over.
        """
        self.iterator = iter(data)
        self.count = 0

    def get_count(self):
        """Returns the current number of items fetched."""
        return self.count

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.
        Raises StopIteration if there are no more items.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
