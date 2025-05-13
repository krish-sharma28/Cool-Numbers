import sys
import random
from expression_validator import validate_expression
from leaderboard import update_leaderboard
from hint_generator import generate_hint
class Creation:
    """
        Handles creation of unique 4-card hands from a deck of cards.
        This class maintains a full deck of cards and ensures that newly drawn 
        hands are unique with respect to recently drawn hands.

        Attributes:
            full_deck (list of int): The deck of cards from 1 to 9, with a total of 36-card deck.
            recent_hands (list of tuple): A list of previously drawn hands (each as 
                a sorted 4-card tuple) to ensure uniqueness when drawing new hands.
        Side Effects:
            The `draw_unique_hand` method modifies the `recent_hands` list by appending any newly drawn unique hand.
        Raises:
            ValueError: If there are fewer than 4 cards in the deck.
            Exception: If a unique hand cannot be found within the maximum number of attempts.
    """

    def __init__(self):
        """
        Draws a unique 4-card hand from the full deck that has not been used recently
        
        Args:
            full_deck (list of int): Contains four copies of each number from 1 to 9.
            recent_hands (list of tuple): Stores recently drawn unique hands to avoid repeats. 
        """
        self.full_deck = [val for val in range(1, 10) for _ in range(4)]
        self.recent_hands = []

    def draw_unique_hand(self, max_attempts=100):
        """
        Draw a unique 4-card hand from the given deck that has not been used recently.

        Args:
            max_attempts (int): Maximum number of attempts to find a unique handm default is 100.

        Returns:
            list of int: A 4-card hand not in recent_hands
        Raises:
            ValueError: If there are fewer than 4 cards in the deck.
            Exception: If a unique hand could not be found within the specified 
                number of attempts.    
        """
        if len(self.full_deck) < 4:
            raise ValueError("Not enough cards in the deck to draw a hand.")
        
        for _ in range(max_attempts):
            hand = random.sample(self.full_deck, 4)  
            hand_tuple = tuple(sorted(hand))

            if hand_tuple not in self.recent_hands: 
                self.recent_hands.append(hand_tuple)
                return hand
        raise Exception("Failed to find a unique hand after max attempts.")    

def card():
    """
    Prompts for player names and the number of rounds to play for the Rounds mode.
    This function collects the names of players and ensures that a valid 
    number of rounds is input by the user. It returns the list of player names 
    and the number of rounds to be played.

    Returns:
        tuple: A tuple containing:
            - list of str: The names of the players.
            - int: The number of rounds to be played.
    Raises:
        ValueError: If the input for rounds is not a valid positive integer.
    """
    players = []
    while True:
        name = input("Enter the name of a player (or type 'done'): ")
        if name.lower() == 'done':
            break
        players.append(name)
    
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds > 0:
                break
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Enter a valid number.")
    
    return players, rounds

def play_game(players, rounds):
    """
    Plays the card game for the specified number of rounds with the given players.
    This function draws hands, validates solutions, and keeps track of player scores. After each round, it updates the scores and prints the final results at the end.

    Args:
        players (list of str): The list of player names.
        rounds (int): The number of rounds to play.
    Side Effects:
        - Updates and prints the final scores after all rounds are completed.
        - Updates the leaderboard with the most recent scores.
    Raises:
        ValueError: If the player name entered is not valid or the solution is invalid.
    """

    game = Creation()
    scores = {player: 0 for player in players}

    for r in range(1, rounds + 1):
        print(f"\nRound {r}")
        hand = game.draw_unique_hand()
        print(f"Your hand: {hand}")

        player_name = input("Who solved it? (Enter name or 'skip'): ")
        if player_name.lower() == 'skip':
            print("No one scored this round.")
            continue
        if player_name not in scores:
            print("Invalid player name.")
            continue
        
        hint_used = False

        while True:
            solution = input("Enter your solution (or type 'hint'): ").strip()
            if solution.lower() == "hint":
                if not hint_used:
                    print(generate_hint(hand))
                    hint_used = True
                else:
                    print("You've already used your hint this round.")
                continue
            is_correct = validate_expression(solution, hand)
            
            if is_correct:
                scores[player_name] += 1000
                break  # exit loop on correct answer
            else:
                break 
            
            
            
    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")
    
    update_leaderboard(player, score, mode='rounds')

