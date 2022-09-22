"""An excercise in writing tests in python. This is where the tests will be contained."""

__author__ = '730556651'


from utils import only_evens, concat, sub


# # ===========================================================================================

# Testing the function 'only_evens'

def test_only_evens_empty() -> None:
    """Tests if returns an empty string when given an empty string."""
    assert only_evens([]) == []

def test_only_evens_only_odd() -> None:
    """Ensures function returns an empty string when no evens present."""
    assert only_evens([1, 3, 5, 7, 9]) == []

def test_only_evens_odd_and_even() -> None:
    """Tests that function works when given a list of both even and odds."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


# ===========================================================================================

# Testing the function 'concat'

def test_concat_empty() -> None:
    """Asserts that when given two empty strings function returns an empty string."""
    assert concat([], []) == []

def test_concat_does_not_mutate() -> None:
    """Asserts that function does not mutate original lists."""
    xs: list[int] = [1, 2, 3, 4]
    xt: list[int] = [5, 6, 7, 8]
    assert xs == [1, 2, 3, 4]
    assert xt == [5, 6, 7, 8]

def test_concat_correct_order() -> None:
    """Asserts that function adds list one after the other."""
    xs: list[int] = [1, 2, 3, 4]
    xt: list[int] = [5, 6, 7, 8]
    assert concat(xs, xt) == [1, 2, 3, 4, 5, 6, 7, 8]


# ===========================================================================================

# Tests function 'sub'

def test_sub_length_one() -> None:
    """Ensures when given a list of length one 'sub' behaves properly."""
    assert sub([35], 0, 1) == [35]

def test_sub_exclusive() -> None:
    """Ensures that sub leaves out the y index."""
    assert len(sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 8)) == 5

def test_sub_doesnt_modify() -> None:
    """Ensures sub does not modify original list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    sub(xs, 0, 4)
    assert xs == [1, 2, 3, 4, 5, 6, 7, 8]