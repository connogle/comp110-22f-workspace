"""An example of a list utility algorithm."""

from random import randint
#Name: contains
# Function with two parameters:
#   needele - what we are looking for
#   haystack - what we are sorting through
#return type: bool

# Start from first index
# Loop through each index of list
#   Test if equal to needle
#      Yes! Return True
# Return False

names: list[str] = ['Kevin Bacon', 'Charles', 'Geoffery', 'Kris']

testable: list[str] = list()

counter: int = 0

while counter < 10:
    testable.append(names[randint(0,3)])
    counter += 1



def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack) - 1:
        if needle == haystack[i]:
            return True
        i += 1
    return False

print(contains('Kevin Bacon', names))