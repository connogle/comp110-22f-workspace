colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}


def favorite_color(colors: dict[str, str]) -> str:
    """Returns a string with the most frequent favorite color, or really any string value, in a dictionary of two strings."""
    color_number: dict[str, int] = {}
    max: int = 0
    fav_color: str = ''
    for key in colors:
        if colors[key] in color_number:
            color_number[colors[key]] += 1
        else:
            color_number[colors[key]] = 1
    for key in color_number:
        if color_number[key] > max:
            fav_color = key
    return fav_color



print(favorite_color(colors))


