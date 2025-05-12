from time import time
from creation_and_rounds_mode import Creation
from expression_validator import validate_expression
from leaderboard import update_leaderboard

def timed_mode():
    """
    Runs the timed game mode where the player has 90 seconds to 
        solve as many hands as possible.

    Side effects:
    - Prints hands, game prompts, and time remaining to the console.
    - Asks the player to enter their name at the end of the game.
    - Updates the 'leaderboard_timed.txt' file with the player's name and score.
    
    """
    start = time()
    score = 0
    game = Creation()
    name = input("Enter your name: ")


    
    while True:
        now = time()
        elapsed = now - start
        if elapsed >= 90:
            break

        print(f"\nTime Remaining: {int(90 - elapsed)} seconds")
        hand = game.draw_unique_hand()
        print(f"Your Hand: {hand}")

        while True:
            user_in = input("Enter your solution (or type 'skip' to skip\
 to the next hand): \n").strip().lower()

            if user_in == 'skip':
                print("Skipping to next hand...")
                break

            if validate_expression(user_in, hand):
                score += 1000
                break
            else:
                print("Incorrect. Try again.")

            now = time()
            elapsed = now - start
            if elapsed >= 90:
                break
            print(f"Time Remaining: {int(90 - elapsed)} seconds")

    print(f"\n Time's up! Final Score: {score}")
    update_leaderboard(name, score, mode='timed')