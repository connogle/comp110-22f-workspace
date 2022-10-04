"""Choose your own adventure. Snail Simulator!!"""

__author__ = '730556651'


# Little happy home for lovely global vars and inputs
from random import randint
points: int = 0
player: str = ''
SNAIL: str = '\U0001F40C'
GROUSE: str = '\U0001F426'

def main() -> None:
    """Allows the game to be a game by making a nice function and procedure soup."""
    global points
    global player
    global SNAIL
    # GROUSE_NUMBER summons a grouse to attack the player. Chances are 1 in 10.
    GROUSE_NUMBER: int = 4
    grouse_chance: int = 0
    TREE: str = '\U0001F332'
    GROUND: str = '\U0001F3DE'
    greet()
    playing: bool = True
    path: str = ''
    # Game Loop, continues running the game unless the player chooses to end or is ended by a grouse
    while playing:
        path = input(f'Okay { player }, what would you like to do now? \n1: Look for food in a tree { TREE }\n2: Look for food on the ground { GROUND }\n3: Finish your snail-tastic adventure as you are satisfied with { points } morsels of food { SNAIL }\n\n')
        grouse_chance = randint(1, 10)
        if path == '1':
            look_in_tree()
            # Grouse encounters have a random chance of occurring after you have chosen a food to take
            if grouse_chance == GROUSE_NUMBER:
                grouse_protocol()
        elif path == '2':
            points = look_on_ground(points)
            if grouse_chance == GROUSE_NUMBER:
                grouse_protocol()
        elif path == '3':
            # Ends the game and reveals the player's score to them
            print(f'\nThank you so much for playing { player }, you had a truly wonderous adventure, collecting { points } morsels of food. \nUnfortunately, however, you will forever be stuck as a snail. Enjoy!')
            playing = False
        else:
            print('\nSorry, that was an invalid submission. Please type just the corresponding number for what you would like to do!\n')


def greet() -> None:
    """Introduces the player to the game and tells them the premise."""
    # global variables and constants needed to greet
    global SNAIL
    global GROUSE    
    global player
    print(f'Well I don\'t know how you got here, but you\'re a snail now { SNAIL }! \nWhile this may seem shocking, I promise it isn\'t too bad! \nYour goal is simply to collect yummy food, and as much of it as you can. \nWhile doing so you must survive random grouse attacks! { GROUSE }\nYou will be given a series of choices numbered 1-3 to determine how to do so using your two very powerful snail brain cells.\n')
    player = input('Now before we begin our snail-tastic adventure, what should I call you? \n\n')
    print(f'\n{ player }? What a lovely name! Now we are going to begin our adventure!\n\n')


# A procedure that uses the player's choices to reassign the points global var
def look_in_tree() -> None:
    """The options for food you have in the tree. Works by reassigning global vars."""
    global player
    global points
    # Using named constants to represent emoji
    BARK: str = '\U0001FAB5'
    LEAF: str = '\U0001F343'
    STEM: str = '\U0001F33F'
    tree_search: bool = True
    food_amount: int = 0
    food_type: str = ''
    food_num: str = ''
    while tree_search:
        food_num = input(f'\n\nOkay { player }, what type of food would you like from the tree? \nYour choices are:\n1: Bark { BARK }\n2: Leaves { LEAF }\n3: Stems { STEM }\n\n')
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


# A function that takes in the global points var as an argument, and uses it as a local var to reassign values before returning the modified value
def look_on_ground(points: int) -> int:
    """The options for searching for food on the ground. Works by reassigning local vars."""
    global player
    MUSHROOM: str = '\U0001F344'
    LETTUCE: str = '\U0001F96C'
    DETRITUS: str = '\U0001F341'
    ground_search: bool = True
    food_amount: int = 0
    food_type: str = ''
    food_num: str = ''
    while ground_search:
        food_num = input(f'\n\nOkay { player } what type of food would you like from the roomy ground? \nYour choices are: \n1: Mushrooms { MUSHROOM }\n2: Lettuce { LETTUCE }\n3: Detritus { DETRITUS }\n\n')
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


# A procedure to trip the player up. This can result in the player losing, surviving but losing points, or surviving without losing any points.
def grouse_protocol() -> None:
    """Determines the consequences of a grouse encounter."""
    global points
    global player
    global GROUSE
    CAUTION: str = '\U00002757'
    SPOON: str = '\U0001F944'
    grouse_attack: bool = True
    print(f'{ CAUTION * 2 }Oh no! A Wild grouse is approaching! { GROUSE } { CAUTION * 2 }\nYou need to act fast, { player }! \nWill you: \n1: Cuddle the very hungry predatory bird \n2: Collapse into your shell and cry for your mommy \n3: Run for your little snail life \n')
    while grouse_attack:
        grouse_reaction: str = input('')
        if grouse_reaction == '1':
            # The player does not survive, ending their run by grouse protocol
            print(f'The grouse is not as interested in cuddling as you are, and devours you. Ironically, using a very little spoon. { SPOON }\nYou had a good run though, { player }, ending with { points } morsels of yummy food.')
            grouse_attack = False
            exit()
        elif grouse_reaction == '2':
            # The player survives and loses no points
            print(f'Wow, { player }, that somehow worked! The grouse ignored both you and your morsels. \n\n')
            grouse_attack = False
        elif grouse_reaction == '3':
            # The player survives, but loses a good deal of points
            points //= 2
            print(f'Fwoo, { player }, you made it out of there! \nUnfortunately though you left some of your food behind! \nThis leaves you with { points } morsels. \n\n')
            grouse_attack = False
        else:
            print('\nSorry, that was an invalid submission. Please type just the corresponding number for what you would like!')
    

if __name__ == '__main__':
    main()