"""EX01 - Chardle - A cute little baby step toward Wordle."""

__author__ = '730556651'

user_word: str = input('Enter a 5-character word: ')
if len(user_word) != 5:
    print('Error: Word must contain 5 characters')
    exit()

user_character: str = input('Enter a single character: ')
if len(user_character) != 1:
    print('Error: Character must be a single character.')
    exit()
print('Searching for ' + user_character + ' in ' + user_word)

character_instances: int = 0
index_number: int = 0

if user_character == user_word[index_number]:
    character_instances += 1
    print(user_character + ' found at index ' + str(index_number))
index_number += 1
if user_character == user_word[index_number]:
    character_instances += 1
    print(user_character + ' found at index ' + str(index_number))
index_number += 1
if user_character == user_word[index_number]:
    character_instances += 1
    print(user_character + ' found at index ' + str(index_number))
index_number += 1
if user_character == user_word[index_number]:
    character_instances += 1
    print(user_character + ' found at index ' + str(index_number))
index_number += 1
if user_character == user_word[index_number]:
    character_instances += 1
    print(user_character + ' found at index ' + str(index_number))
    
if character_instances > 0:
    print(str(character_instances) + ' instances of ' + user_character + ' found in ' + user_word)
else:
    print('No instances of ' + user_character + ' found in ' + user_word)
