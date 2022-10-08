"""In calss code-writing."""


def zip(key: list[str], value: list[str]) -> dict[str, str]:
    """Zips two lists together into a nice little dictionary."""
    assert len(key) == len(value)
    zipped: dict[str, str] = {}
    for i in key:
        zipped[key[i]] = value[i]
    return zipped