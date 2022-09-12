"""Having trouble with the autograder so isolating a function into it's own program to make testing easier."""

from exercises.ex03_wordle import contains_char


def emojified(secret: str, guess: str) -> str:
    """Returns a string with corresponding character placement correctness in emoji form."""
    assert len(guess) == len(secret)
    pretty_boxes: str = ''
    i: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i < len(secret):
        if guess[i] == secret[i]:
            pretty_boxes += GREEN_BOX
        elif contains_char(secret, guess[i]):
            pretty_boxes += YELLOW_BOX
        else:
            pretty_boxes += WHITE_BOX
        i += 1
    return pretty_boxes

if __name__ == "__main__":
    emojified('codes', input())