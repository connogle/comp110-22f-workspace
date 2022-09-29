"""An example of setting up and using for __in__ syntax."""

names: list[str] = ['Kris', 'Kaki', 'Ezri', 'Adin']


# An example of using boring outdated while loop
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1


# Following for __in__ loop is the same as the while loop above
for name in names:
    print(name)