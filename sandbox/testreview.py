

def odd_and_even(nums: list[int]) -> list[int]:
    result: list[int] = []
    i: int = 0
    while i < len(nums):
        if i % 2 == 0 and nums[i] % 2 != 0:
            result.append(nums[i])
        i += 1
    return result

test: list[int] = [2, 9, 4, 17, 9, 10, 15, 13, 14, 21]

print(test)
print(odd_and_even(test))