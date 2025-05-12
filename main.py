import webbrowser
import sys
import random
from expression_validator import validate_expression
from timed_mode import timed_mode
from creation_and_rounds_mode import Creation, card, play_game
from leaderboard import show_leaderboard


def intro():
    """ Logic for the introduction to the game. Allows user to pick between
    leaderboard, rules, play, or exit.
    Prompts the user in a loop until a valid option is selected.
    
    Side effects:
        - Calls play_game(), timed_mode(), show_leaderboard(), help()
        - Prints to console.
    
    """
    key = 0
    welcome_string = """========================================================
Welcome to 24!\n 
The game of adding, subtracting, multiplying, 
and dividing 4 numbers to reach 24.
========================================================\n"""

    # handle logic for leaderboard, help, and play
    while key == 0:
        print(welcome_string)
        gather = input("""What would you like to do? \nOptions:
        - leaderboard
        - rules
        - play
        - exit\n""")
        
        if gather.lower() == 'leaderboard':
            mode = input("Do you want to see Timed or Rounds leaderboard? ")
            try:
                show_leaderboard(mode.lower())
            except:
                print("Not a mode! Try Timed or Rounds")
                intro()
        elif gather.lower() == 'rules' or gather.lower() == 'help':
            help()
        elif gather.lower() == 'play':
            mode = input("Which to play: Timed or Rounds? ")
            if mode.lower()=="rounds":
                players, rounds = card()
                key = 1
                play_game(players, rounds)
            elif mode.lower()=="timed":
                timed_mode()
            else:
                print("Not a mode! Try Timed or Rounds")
                intro()
            break
        elif gather.lower() == 'exit':
            return print("Exiting program.")
            break
        else:
            print(f"{gather} is not a recognized option!\n")


def help():
    """ Prints out rules from a txt file.
    
        Side effects:
            - Reads from file
            - Opens a browser window if 'more' is entered
            - Prints to console
    """
    site = "https://vimeo.com/1013357391" #site that has rules for game
    
    with open("helpstring.txt", "r") as file: #helpstring.txt contains help
        contents = file.read()
        print(contents)
    
    gather = input("What would you like to do? ")
    #conditional expression yippee    
    webbrowser.open_new(site) if gather.lower() == "more" else None 
    return

if __name__ == "__main__":
    intro()