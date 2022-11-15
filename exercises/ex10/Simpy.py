"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730556651"


class Simpy:
    """Simpy class, simple implementation of numpy."""
    values: list[float]

    def __init__(self, rhs: list[float]):
        """Gives values to an object of type Simpy's value attribute."""
        self.values = rhs

    def __repr__(self) -> str:
        """Gives a representation of a Simpy object as a str."""
        return f"Simpy({self.values})"

    def fill(self, fill: float, amt: int) -> None:
        """Fills a Simpy object's value attribute with a list of a certain amount of a certain value."""
        result: list[float] = []
        for _ in range(amt):
            result.append(fill)
        self.values = result

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Gives all values between a start and stop given a step."""
        assert step != 0.0
        result: list[float] = []
        if step > 0:
            assert start < stop
            while start < stop:
                result.append(start)
                start += step
        else:
            assert start > stop
            while start > stop:
                result.append(start)
                start += step
        self.values = result

    def sum(self) -> float:
        """Returns the sum of a Simpy object's values."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Makes adding with a simpy object possible."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(rhs.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Makes exponents with a simpy object possible."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(rhs.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produces a string of bools based on equality of values."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(rhs.values)):
                result.append(self.values[i] == rhs.values[i])
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produces a string of bools based on if self is greater than rhs."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(rhs.values)):
                result.append(self.values[i] > rhs.values[i])
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows subscription notation for a Simpy type."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self[i])
            return result