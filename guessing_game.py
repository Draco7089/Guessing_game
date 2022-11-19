"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    status = True
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    print("\t\tWELCOME PLAYER!")
    random_number = random.randint(0, 10)
    tries = 0
    try:
        player_input = int(input("Enter a number between 0 & 10 >>> "))
        while status:

            if player_input == random_number:
                print("Got it\n")
                print("Thanks for playing! ")
                print("It took {} tries".format(tries))

                status = False
            elif player_input < random_number:
                player_input = int(input("It's higher >>> "))
                tries += 1

            elif player_input > random_number:
                player_input = int(input("It's lower >>> "))
                tries += 1
    except ValueError:
        print("try again")
        start_game()



# Kick off the program by calling the start_game function.
start_game()