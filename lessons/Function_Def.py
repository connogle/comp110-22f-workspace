"""Example of defining a function!!!"""

def my_max(a: int, b: int) -> int:
    """returns the greatest argument."""
    if a>= b:
        return a
    else:
        return b

x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)