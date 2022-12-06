"""Testing written functions."""

from code_writing import reverse_multiply, free_biscuits, multiples,merge_lists, reverse_string, HotCocoa, TimeSpent, factorial


print(reverse_multiply([1, 2, 3]))
print(free_biscuits({ "UNCvsDuke": [38, 20, 42] , "UNCvsState": [9, 51, 16, 23] }))
print(multiples([2, 3, 4, 8, 16, 2, 4, 2]))
print(merge_lists(["blue", "yellow", "red"], [5, 2, 4]))
print(reverse_string('door'))

cocoa: HotCocoa = HotCocoa(True, "vanilla", 8, 4)
print(cocoa.calorie_count())
cocoa.mallow_adder(8)
print(cocoa.calorie_count())

time: TimeSpent = TimeSpent("Tori", "Studying", 200)
print(time.report())
time.add_time(60)
print(time.reset())
print(time.report())

print(factorial(5))