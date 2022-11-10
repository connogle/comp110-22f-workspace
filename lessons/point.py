"""something for a silly little lesson."""

class Point:
    
    X: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: float):
        return Point(self.x * factor, self.y * factor)

    # def __str__(self) -> str:
    #     """Produce a str representation of an object of a Point for humans."""
    #     return f"({self.x}, {self.y})"

    def __mul__(self, factor: float):
        return Point(self.x * factor, self.y * factor)

    def __repr__(self) -> str:
        """Creates a string representation of a Point for Python!"""
        return f"Point({self.x}, {self.y})"

    def __add__(self, rhs):
        return Point(self.x + rhs.x, self.y + rhs.y)

p0: Point = Point(1.0, 2.0)
p1: Point = p0 * 4.0

print(p0)

p0_repr: str = repr(p0)
print(p0_repr)

print(p0 + p1)