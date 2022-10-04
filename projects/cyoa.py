"""Choose your own adventure. Snail Simulator!!"""

__author__ = '730556651'

# Little happy home for lovely global vars and inputs

from random import randint
points: int = 0
player: str = ''
# GROUSE_NUMBER summons a grouse to attack the player. Chances are 1 in 12.
GROUSE_NUMBER: int = 4


def main() -> None:
    """Allows the game to be a game by making a nice function and procedure soup."""
    global points
    global player
    global GROUSE_NUMBER
    greet()
    playing: bool = True
    path: str = ''
    while playing:
        path = input(f'Okay { player }, what would you like to do now!? \n1: Look for food in a tree \n2: Look for food on the ground \n3: Finish your snail-tastic adventure as you are satisfied with { points } morsels of food\n\n')
        if path == '1':
            look_in_tree()
            if randint(1, 12) == GROUSE_NUMBER:
                grouse_protocol()
        elif path == '2':
            points = look_on_ground(points)
            if randint(1, 12) == GROUSE_NUMBER:
                grouse_protocol()
        elif path == '3':
            print(f'\nThank you so much for playing { player }, you had a truly wonderous adventure, collecting { points } morsels of food. \nUnfortunately, however, you will forever be stuck as a snail. Enjoy!')
            playing = False
        else:
            print('\nSorry, that was an invalid submission. Please type just the corresponding number for what you would like to do!\n')
    return None


def greet() -> None:
    """Introduces the player to the game and tells them the premise."""
    print('Well I don\'t know how you got here, but you\'re a snail now! \nWhile this may seem shocking, I promise it isn\'t too bad! \nYour goal is simply to collect yummy food, and as much of it as you can. \nWhile doing so you must survive random grouse attacks! \nYou will be given a series of choices numbered 1-3 to determine how to do so using your two very powerful snail brain cells.\n')
    global player
    player = input('Now before we begin our snail-tastic adventure, what should I call you? \n\n')
    print(f'\n{ player }? What a lovely name! Now we are going to begin our adventure!\n\n')
    return None


def look_in_tree() -> None:
    """The options for food you have in the tree. Works by reassigning global vars."""
    global player
    global points
    tree_search: bool = True
    food_amount: int = 0
    food_type: str = ''
    food_num: str = ''
    while tree_search:
        food_num = input(f'\n\nOkay { player }, what type of food would you like from the tree? \nYour choices are:\n1: Bark \n2: Leaves \n3: Stems\n\n')
        if food_num == '1':
            food_amount += randint(1, 5)
            food_type = 'Bark'
            tree_search = False
        elif food_num == '2':
            food_amount += randint(1, 5)
            food_type = 'Leaves'
            tree_search = False
        elif food_num == '3':
            food_amount += randint(1, 5)
            food_type = 'Stems'
            tree_search = False
        else:
            print('\nSorry, that was an invalid submission. Please type just the corresponding number for what you would like!')
    points += food_amount
    print(f'\nWow, you found { food_amount } morsels of { food_type } in a tree! \n Great job { player }! \nThat brings your total amount of food to { points } morsels!\n\n')


def look_on_ground(points: int) -> int:
    """The options for searching for food on the ground. Works by reassigning local vars."""
    global player
    ground_search: bool = True
    food_amount: int = 0
    food_type: str = ''
    food_num: str = ''
    while ground_search:
        food_num = input(f'\n\nOkay { player } what type of food would you like from the rommy ground? \nYour choices are: \n1: Mushrooms \n2: Lettuce \n3: Detritus \n\n')
        if food_num == '1':
            food_amount += randint(1, 5)
            food_type = 'Mushrooms'
            ground_search = False
        elif food_num == '2':
            food_amount += randint(1, 5)
            food_type = 'Lettuce'
            ground_search = False
        elif food_num == '3':
            food_amount += randint(1, 5)
            food_type = 'Detritus'
            ground_search = False
        else:
            print('\nSorry, that was an invalid submission. Please type just the corresponding number for what you would like!')
    points += food_amount
    print(f'\nWow, you found { food_amount } morsels of { food_type } on the ground! \n Great job { player }! \nThat brings your total amount of food to { points } morsels!\n\n')
    return points


def grouse_protocol() -> None:
    """Determines the consequences of a grouse encounter."""
    global points
    global player
    grouse_attack: bool = True
    print(f'Oh no! A Wild grouse is approaching! \nYou need to act fast, { player }! \nWill you: \n1: Cuddle the very hungry predatory bird \n2: Collapse into your shell and cry for your mommy \n3: Run for your little snail life \n')
    while grouse_attack:
        grouse_reaction: str = input('')
        if grouse_reaction == '1':
            print(f'The grouse is not as interested in cuddling as you are, and devours you. Ironically, using a very little spoon. \nYou had a good run though, { player }, ending with { points } morsels of yummy food.')
            grouse_attack = False
            exit()
        elif grouse_reaction == '2':
            print(f'Wow, { player }, that somehow worked! The grouse ignored both you and your morsels.')
            grouse_attack = False
        elif grouse_reaction == '3':
            points /= 2
            print(f'Fwoo, { player }, you made it out of there! \nUnfortunately though you left half of your food behind! \nThis leaves you with { points } morsels.')
        else:
            print('\nSorry, that was an invalid submission. Please type just the corresponding number for what you would like!')
    


if __name__ == '__main__':
    main()