import sys
import random
from expression_validator import validate_expression
from leaderboard import update_leaderboard
class Creation:
    def __init__(self):
        # Instance attributes
        self.full_deck = [val for val in range(1, 10) for _ in range(4)]
        self.recent_hands = []

    def draw_unique_hand(self, max_attempts=100):
        """
        Draw a unique 4-card hand from the given deck that has not been used recently.

        Parameters:
            deck (list of int): The current available cards in the deck.
            recent_hands (list of tuple): A list of recently used hands, sorted (e.g., [(1, 2, 3, 4)])
            max_attempts (int): Maximum number of attempts to find a unique hand

        Returns:
            list of int: A 4-card hand not in recent_hands
            or raises an Exception if unable to find a unique hand
        """
        if len(self.full_deck) < 4:
            raise ValueError("Not enough cards in the deck to draw a hand.")
        
        for _ in range(max_attempts):
            hand = random.sample(self.full_deck, 4)  # Randomly draw 4 cards
            hand_tuple = tuple(sorted(hand))

            if hand_tuple not in self.recent_hands:  # Ensure it's a unique hand
                self.recent_hands.append(hand_tuple)
                return hand
        raise Exception("Failed to find a unique hand after max attempts.")    
def card():
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

        solution = input("Enter your solution: ")
        if validate_expression(solution, hand): 
            scores[player_name] += 1000
        else:
            print("Incorrect.")
    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")
    
    update_leaderboard(player, score, mode='rounds')

