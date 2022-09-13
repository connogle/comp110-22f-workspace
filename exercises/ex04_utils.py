"""Creating well known functions using list functionality."""

__author__ = '730556651'


# Determines whether or not all of the ints in a list are the same as a given int
def all(numbs: list[int], test: int) -> bool:
    """Determines if the ints in a list are ALL equal to a given int."""
    i: int = 0
    if len(numbs) == 0:
        return False
    while i < len(numbs):
        if numbs[i] != test:
            return False
        i += 1
    return True


# Determines the largest int in a list by using relational operators
def max(a: list[int]) -> int:
    """Finds the maximum value in a list of ints."""
    if len(a) == 0:
        raise ValueError('max() arg is an empty list')
    while len(a) > 1:
        if a[0] > a[len(a) - 1]:
            a.pop(len(a) - 1)
        else:
            a.pop(0)
    return a[0]


# Determines if two lists of equal length are equal at every index
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Tells if two strings are equal."""
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True
