"""An exercise in creating a short version of wordle."""

__author__ = '730556651'

secret_word: str = 'python'
word_length: int = len(secret_word)
user_guess: str = input(f'What is your { str(word_length) }-letter guess? ')

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(user_guess) != word_length:
    user_guess = input(f'That was not { str(word_length) } letters! Try again: ')
   
index_number: int = 0
colorful_squares: str = ''

while index_number < word_length:
    current_character: str = user_guess[index_number]

    if current_character == secret_word[index_number]:
        colorful_squares += GREEN_BOX
    else:
        instance_counter: int = 0

        while instance_counter < word_length:
            if current_character == secret_word[instance_counter]:
                colorful_squares += YELLOW_BOX
                instance_counter += word_length
            else:
                instance_counter += 1
        if len(colorful_squares) == index_number:
            colorful_squares += WHITE_BOX
    index_number += 1

print(colorful_squares)
if colorful_squares == GREEN_BOX * word_length:
    print('Woo! You got it!')
else:
    print('Not quite. Play again soon!')
