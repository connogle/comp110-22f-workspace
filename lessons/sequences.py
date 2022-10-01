"""Writing new forms of sequences."""

# Tuple sequences!!!
# Declaring a type alias that 'invents' the point2D type
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
print(start_position)
end_position: Point2D = (99.0, 99.0)


# tuples, because they are a sequence, are zero indexed
print(start_position[0])

for item in end_position:
    print(item)

# Ranges!
aa_range: range = range(0, 27, 2)
print(aa_range[1])

for i in range(0, 33, 3):
    print(i)

names: list[str] = ['Kris', 'Alyssa', 'Ben', 'Arnold']
for i in range(0, len(names), 2):
    print(names[i])