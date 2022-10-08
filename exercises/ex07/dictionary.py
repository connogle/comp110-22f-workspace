"""Where functions and implementations will go for ex07."""

__author__ = '730556651'


# Invert Function
def invert(original: dict[str, str]) -> dict[str, str]:
    """Rerturns a dictionary that swaps the key and value of another dictionary."""
    inverse: dict[str, str] = {}
    for key in original:
        if original[key] in inverse:
            raise KeyError
        inverse[original[key]] = key
    return inverse


# Favorite Colors Function
def favorite_color(colors: dict[str, str]) -> str:
    """Returns a string with the most frequent favorite color, or really any string value, in a dictionary of two strings."""
    number_of_color: dict[str, int] = {}
    max: int = 0
    fav_color: str = ''
    for key in colors:
        if colors[key] in number_of_color:
            number_of_color[colors[key]] += 1
        else:
            number_of_color[colors[key]] = 1
    for key in number_of_color:
        if number_of_color[key] > max:
            fav_color = key
            max = number_of_color[key]
    return fav_color


# Count function
def count(strings: list[str]) -> dict[str, int]:
    """Places the items in a list of strings into a dictionary displaying their frequencies."""
    result: dict[str, int] = {}
    for string in strings:
        if string in result:
            result[string] += 1
        else:
            result[string] = 1
    return result