"""A more functional version of worlde."""


__author__ = '730556651'


# The characters that aren't in their correct instances are being analyzed to see if they exist elsewhere
def contains_char(word: str, char: str) -> bool:
    """Asserts if a single character in the user's guess is present in secret word."""
    assert len(char) == 1
    i: int = 0
    word_length: int = len(word)
    while i < word_length:
        if char == word[i]:
            return True
        else:
            i += 1
    return False


# The characters are being assignes emoji blocks with their corresponding meanings
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
    

# The program is taking an input from the user only if it matches the corect number of characters
def input_guess(expected_length: int) -> str:
    """This asks a user for a str value, ensures that it is the right length, then returns the input."""
    guess: str = input(f'Enter a { expected_length } character word: ')
    while len(guess) != expected_length:
        guess = input(f'That wasn\'t { expected_length } chars! Try again: ')
    return guess


# All of the other functions are assembled and structured in a way that creates a workable wordle
def main() -> None:
    """The big block that makes this work."""
    secret_word: str = 'codes'
    attempts: int = 1
    playing: bool = True
    while attempts < 7 and playing is True:
        print(f'=== Turn { attempts }/6 ===')
        user_guess = input_guess(len(secret_word))
        print(emojified(secret_word, user_guess))
        if user_guess == secret_word:
            playing = False
        else:
            attempts += 1
    if attempts < 7:
        print(f'You won in { attempts }/6 turns!')
    else:
        print('X/6 - Sorry, try again tomorrow!')


if __name__ == "__main__":
    main()

    