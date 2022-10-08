"""Unit tests for ex07's dictionary module."""

__author__ = '730556651'


# Import Area!!
from dictionary import invert, favorite_color, count
import pytest


# Testing for the function 'invert'

def test_invert_empty_string() -> None:
    """Edge case for 'invert', tests when given empty list."""
    assert invert({}) == {}


def test_invert_inverts_multiple_values() -> None:
    """Ensures that invert works with a dictionary containing multiple keys-value pairs."""
    test: dict[str, str] = {'one': '1', 'two': '2', 'three': '3', 'four': '4'}
    test_inverted: dict[str, str] = {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
    assert invert(test) == test_inverted


def test_invert_raises_key_error() -> None:
    """Ensures that invert is rasing key error in appropriate situation."""
    with pytest.raises(KeyError):
        invert({'silver': 'bells', 'jingle': 'bells'})


# Testing for the function 'favorite_color'

def test_favorite_color_empty_dict() -> None:
    """Ensures that if given an empty dictionary favorite_color returns an empty string."""
    assert favorite_color({}) == ''


def test_favorite_color_multiple_even_value() -> None:
    """When there are two colors tied for the most abundant favorite_color returns the one which appears first in dict."""
    color_example: dict[str, str] = {'Einstein': 'purple', 'Hawking': 'purple', 'Cretin': 'anything else', 'Dunce': 'anything else'}
    assert favorite_color(color_example) == 'purple'


def test_favorite_color_many_vals() -> None:
    """Ensures that when given a dictionary with many varying values favorite_color doesn't break."""
    long_example: dict[str, str] = {'1': 'orange', '2': 'violet', '3': 'magenta', '4': 'lavender', '5': 'lavender', '6': 'periwinkle'}
    assert favorite_color(long_example) == 'lavender'


# Testing for the function 'count'

def test_count_empty_list() -> None:
    """Ensures that count returns an empty dict when given an empty list."""
    assert count([]) == {}


def test_count_all_one_value() -> None:
    """Ensures that 'count' works when it's just one string over and over."""
    assert count(['1', '1', '1', '1', '1', '1', '1']) == {'1': 7}


def test_count_many_values() -> None:
    """Makes sure that 'count' functions correctly when given many values."""
    num_list: list[str] = ['1', '2', '2', '3', '3', '3']
    assert count(num_list) == {'1': 1, '2': 2, '3': 3}