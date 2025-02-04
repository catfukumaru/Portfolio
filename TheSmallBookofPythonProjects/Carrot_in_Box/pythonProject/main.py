import random

"""
my_module.py

This module provides functions for completing a program called Carrot in Box.

This is a game for two human players. Each player has a box. One box has a carrot in it, and each 
player wants to have the carrot. The first player looks in their box and then 
tells the second player they either do or don\’t have the carrot. 
The second player gets to decide whether to swap boxes or not. 

Functions:
- ask_pl_name(): Returns the player's name
- add_player(name): adds a variable to a list 
- choose_where_is_carrot(): Returns a boolean signifying with which player is the carrot with
- print_carrot(box1, name1): prints out if the carrot is the first player
- lie_input(): evaluates the input to go into lie_about_carrot(carrot, lie)
- lie_about_carrot(carrot, lie): asks the first player is they want to lie about whether they have the carrot.
- second_player_route(box1, box2): return the variable box1 and box2 swapped with each other or unchanged
- main(): runs all the functions above to create the game

Usage:
    run the file independently
"""

player_names = []

def ask_pl_name():
    ''' 
        asks the user their name
        :return: returns a string with letters representing the user's name
    '''
    
    while True:
        name =  input("please input your name? use only letters \n")

        if name.isalpha():
            return name
        else:
            print(f"'{name}' should only have letters")

def add_player(name):
    '''
        adds the name of the player to  player_names
        :param name = Str
    '''

    global player_names
    if name not in player_names:
        player_names.append(name)
    else:
        print("the name you choose has already been chosen please choose another name")
        ask_pl_name()


def choose_where_is_carrot():
    '''
        Choose a random value from the options variable. The value signifies whether there is a carrot or not in the box
        :return carrot = Int
    '''
    options = [0,1]
    carrot = random.choice(options)
    """ get a ramdom number generator to choose between the numbers in a list. 
    this is done instead of just the numbers so that decimals are not chosen"""
    return carrot

def print_carrot(box1, name1):
    '''
        prints whether the first player has the carrot or not
        :param box1 = Int
        :param name1 = str
    '''
    if box1:
        print(name1 + " has the carrot")
    else:
        print(name1 + " doesn\'t have the carrot")

def lie_input():
    '''
        validate the input from the user so that only 'T' or 'L' are a parameter for def lie_about_carrot
        :return lie = str
    '''
    while True:
        lie = input("Do you want to lie or say the truth? \nrespond with 'T' or 'L' ")
        if lie not in ['T', 'L']:
            print("wrong input. Only 'T' or 'L' are allowed")
        else:
            return lie

def lie_about_carrot(carrot,lie):
    '''
        prints the lie or truth about whether the first player has the carrot
        :param carrot = Boolean
        :param lie = str
    '''
    if carrot:
        if lie == 'T':
            print("I have the carrot")
        if lie == 'L':
            print("I don't have the carrot")

    else:
        if lie == 'T':
            print("I don't have the carrot")
        if lie == 'L':
            print("I have the carrot")


def second_player_route(box1, box2):
    # if it is the second player's turn
    '''
        the function that is only for the second player. They choose to swap the boxes
        :param box1 = Boolean
        :param box2 = Boolean
        :return box1 = Boolean
        :return box2 = Boolean
    '''
    while True:
        swap = input("Second player do you want to swap the boxes? respond with 'Y' or 'N' ")

        if swap == 'Y':
            box1 = not box1
            box2 = not box2
            return box1, box2
        if swap == 'N':
            return box1, box2
        else:
            print(f"The only acceptable input are 'Y' or 'N'")

def main():
    """
    The main entry point of the program.

    This function initializes the application,and orchestrates the main functionality of the program.
    It also contains an explanation of the program.


    Example:
        To run this program, execute the following command:
        Press the run function in your IDE


    """

    print("""
    Hi and welcome to Carrot in Box. This is a simple and silly bluffing game for 
    two human players. Each player has a box. One box has a carrot in it, and each 
    player wants to have the carrot. The first player looks in their box and then 
    tells the second player they either do or don\’t have the carrot. 
    The second player gets to decide whether to swap boxes or not.\n""")

    name1 = ask_pl_name()
    name2 = ask_pl_name()

    add_player(name1)
    add_player(name2)

    box1 = choose_where_is_carrot()
    box2 = not box1

    print_carrot(box1, player_names[0])

    lie = lie_input()

    lie_about_carrot(box1, lie)

    box1, box2 = second_player_route(box1, box2)
    print_carrot(box1, name1)
    print_carrot(box2, name2)


if __name__ == "__main__":
    main()
