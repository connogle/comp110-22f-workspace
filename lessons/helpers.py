"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n

print("helpers.py was evaluated")
