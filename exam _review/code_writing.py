"""File dedicated to writing functions on the study guide."""


def reverse_multiply(orig: list[int]) -> list[int]:
    result: list[int] = []
    i: int = len(orig) - 1
    while i>=0:
        result.append(orig[i]*2)
        i -= 1
    return result


def free_biscuits(stats: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for game in stats:
        score: int = 0
        for points in stats[game]:
            score += points
        if score >= 100:
            result[game] = True
        else:
            result[game] = False
    return result


def multiples(nums: list[int]) -> list[bool]:
    result: list[bool] = []
    result.append(nums[0] % nums[len(nums)-1] == 0)
    for i in range(1, len(nums)):
        result.append(nums[i] % nums[i - 1] == 0)
    return result


def merge_lists(strs: list[str], ints: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    if len(strs) != len(ints):
        return result
    for i in range(len(strs)):
        result[strs[i]] = ints[i]
    return result


def reverse_string(word: str) -> str:
    result: str = ""
    for i in range(len(word) - 1, -1, -1):
        result += word[i]
    return result


class HotCocoa:
    has_whip: bool
    flavor: str
    marshmallow_count: int
    sweetness: int

    def __init__(self, a: bool, b: str, c: int, d: int):
        self.has_whip = a
        self.flavor = b
        self.marshmallow_count = c
        self.sweetness = d

    def mallow_adder(self, adder: int) -> None:
        self.marshmallow_count += adder
        self.sweetness += adder * 2

    def calorie_count(self) -> float:
        calories: float = 0.0
        if self.flavor == "vanilla" or self.flavor == "peppermint":
            calories += 30.0
        else:
            calories += 20.0
        if self.has_whip:
            calories += 100.0
        return calories + self.marshmallow_count / 2


class TimeSpent:
    name: str
    puprose: str
    minutes: int

    def __init__(self, n: str, p: str, m: int):
        self.name = n
        self.purpose = p
        self.minutes = m

    def add_time(self, time: int) -> None:
        self.minutes += time

    def reset(self) -> int:
        result = self.minutes
        self.minutes = 0
        return result

    def report(self) -> str:
        return f"{self.name} has spent {self.minutes // 60} hours and {self.minutes % 60} minutes on {self.purpose}."


def factorial(num: int) -> int:
    if num == 1:
        return num
    return num * factorial(num - 1)