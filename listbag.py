"""
File: listbag.py
Author: Man-Chi Leung
"""


class ListBag(object):
    """A list-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.__elements = []
        if sourceCollection is not None:
            for e in sourceCollection:
                self.add(e)
        a = 0

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return len(self.__elements)

    def __str__(self):
        """Returns the string representation of self."""
        listStr = "{"
        for i in range(len(self.__elements)):
            listStr += "{}".format(self.__elements[i])
            if i < len(self.__elements) - 1:
                listStr += ", "
        listStr += "}"
        return listStr

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self.__elements):
            yield self.__elements[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ListBag(self.__elements)
        for element in other:
            result.add(element)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""

    def count(self, item):
        """Returns the number of instances of item in self."""
        countItems = 0
        for x in self.__elements:
            if x == item:
                countItems += 1
        return countItems

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.__elements = []

    def add(self, item):
        """Adds item to self."""
        self.__elements.append(item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if item not in self:
            raise KeyError("{} not in set".format(item))
        else:
            self.__elements.remove(item)
