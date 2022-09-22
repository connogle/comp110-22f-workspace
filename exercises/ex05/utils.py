"""An exercise in writing tests in python. Where functions will be written to test for exercise 05."""

__author__ = '730556651'


def only_evens(xs: list[int]) -> list[int]:
    """Takes a list of arbitrary length and returns a list containing only the even numbers."""
    i: int = 0
    even_list: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0:
            even_list.append(xs[i])
        i += 1
    return even_list


def concat(xs: list[int], xt: list[int]) -> list[int]:
    """Takes two lists and creates a new list with the first list's values coming first."""
    concat_list: list[int] = list()
    i: int = 0
    while i < len(xs):
        concat_list.append(xs[i])
        i += 1
    i = 0
    while i < len(xt):
        concat_list.append(xt[i])
        i += 1
    return concat_list    


def sub(xs: list[int], x: int, y: int) -> list[int]:
    """Given a list of ints(xs), a start index(x), and a non-inclusive ending index(y), returns the values in the given range."""
    assert x < len(xs)
    assert x >= 0
    assert len(xs) > 0
    assert y < len(xs)
    sub_list: list[int] = list()
    while x < y:
        sub_list.append(xs[x])
        x += 1
    return sub_list