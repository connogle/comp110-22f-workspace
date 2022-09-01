"""An example of a while loop statemnt."""

counter: int = 0
maximum: int = int(input('count up to but not including what? '))
while counter < maximum:
    counter_squared: int = counter ** 2
    print('The square of ' + str(counter) + ' is ' + str(counter_squared))
    counter += 1

print('done!')