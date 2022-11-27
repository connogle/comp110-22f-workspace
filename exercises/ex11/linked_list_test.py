"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale, is_equal

__author__ = "730556651"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_non_empty() -> None:
    "Selected Value in a non-empty fully-normal linked list."
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_value_at_empty() -> None:
    """Tests that when given an empty linked list value_at raises an index error."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_max_one_item() -> None:
    """A test of the max function's base case."""
    lonely_node: Node = Node(6, None)
    assert max(lonely_node) == 6


def test_max_full_list() -> None:
    """A test of max's normal functionality."""
    linked_list: Node = Node(1, Node(7, Node(3, Node(4, None))))
    assert max(linked_list) == 7


def test_linkify_empty_list() -> None:
    """Asserts that when given an empty list linkify returns None."""
    assert linkify([]) == None


def test_linkify_actual_list() -> None:
    """A test of the normal use of linkify."""
    linked_list = Node(1, Node(2, Node(3, Node(4, None))))
    assert is_equal(linkify([1, 2, 3, 4]), linked_list)


def test_scale_empty() -> None:
    """Tests an empty linked list being sent through scale."""
    assert scale(linkify([]), 3) == None


def test_scale_actual_list() -> None:
    """Tests typical implementation of the scale function."""
    assert is_equal(scale(linkify([1, 2, 3]), 2), linkify([2, 4, 6]))