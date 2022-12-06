import turtle as t
UP: float = 90.0


def happy_tree(x: float, y: float) -> None:
    """Paint a beautiful tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    trunk_length: float = 40.0
    branch(UP, trunk_length)


def branch(angle: float, length: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length >= 5:
        branch(angle + 25.0, length * 0.75)
        branch(angle - 25.0, length * 0.75)
    t.setheading(angle + 180)
    t.forward(length)


t.tracer(0, 0)
t.speed(0)
t.getscreen().onclick(happy_tree)
t.done()