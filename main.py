import webbrowser
import sys
import random
from expression_validator import validate_expression
from timed_mode import timed_mode
from creation_and_rounds_mode import Creation, card, play_game
from leaderboard import show_leaderboard


def main():
    """ Switching name to intro, this is the start and setup of the code.

    
    """
    key = 0
    welcome_string = """Welcome to 24!\n 
The game of adding, subtracting, multiplying, and dividing\
4 numbers to reach 24."""

    # handle logic for leaderboard, help, and play
    while key == 0:
        print(welcome_string)
        gather = input("What would you like to do?\n"
    "Options:\n"
    "- leaderboard\n"
    "- rules\n"
    "- play\n"
    "- exit\n")
        if gather.lower() == 'leaderboard':
            mode=input("Which mode leaderboard do you want to see?")
            show_leaderboard(mode.lower())
        elif gather.lower() == 'rules':
            help()
        elif gather.lower() == 'play':
            mode=input("Choose the mode you want to play: Timed or Rounds")
            if mode.lower()=="rounds":
                players, rounds = card()
                key = 1
                play_game(players, rounds)
            elif mode.lower()=="timed":
                timed_mode()
            break
        elif gather.lower() == 'exit':
            return print("Exiting program.")
        else:
            print("""Not a valid input! Choose between leaderboard, rules, 
and play. Write 'exit' at any time to end program.""")
    # while key == 1:
    #     print("-----------------")
    #     print(f"| {c_result[0]} | {c_result[1]} | {c_result[2]} | {c_result[3]} |")
    #     print("-----------------")
    #     gather = input("Enter your answer in reverse polish notation. ")

    #     if score(gather):
    #         print("Yippee!")
    #         key == 0
    #     elif gather.lower() == 'exit':
    #         return print("Exiting program.")
    #     else:
    #         print("Incorrect! Try Again!")
    #         pass

def leaderboard():
    pass

def help():
    """ Enters the help window, presenting the user with rules and a video.
    
    Side Effects:
    if "more" is typed, player is brought to a video in their browser. 
    """
    site = "https://vimeo.com/1013357391"
    help_string = """
    24 is played by taking 4 numbers and using basic arithmetic operations to
    get to the number 24.\n
    
    After typing 'play' into the prompt box, you will be asked 
    for the mode you want to play:\n
    Timed or Rounds\n
    
    After you choose the mode you want to play, you will be greeted by a hand.
    ----------------- 
    | 2 | 3 | 2 | 4 |  
    -----------------  
    To play you must type in your answer.
    EXAMPLE: (2+2+4)*3
    Still dont understand? To watch a video on the rules, type "more".
    Otherwise, type 'return' """
    print(help_string)
    gather = input("What would you like to do? ")
    if gather.lower() == 'exit':
        print("Exiting program.")
        sys.exit()
    if gather.lower() == "more":
        webbrowser.open_new(site)
        return
    if gather.lower() == "return":
        return
    else:
        print("not an option, oh well.")
        return       


if __name__ == "__main__":
    main()