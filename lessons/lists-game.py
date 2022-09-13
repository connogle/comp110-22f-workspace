"""Example of using lists in a simple 'game'."""


from random import randint


rolls: list[int] = list()


i: int = 0

while len(rolls) == 0 or rolls[i] != 1:
    rolls.append(randint(1, 6))
    i = len(rolls) - 1
print(rolls)

rolls.pop(len(rolls) - 1)
print(rolls)

i = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f'Total score: {sum}')

   
