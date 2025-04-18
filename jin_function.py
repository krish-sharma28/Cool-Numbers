""" The draw_unique_hand funtion draws a unique hand of 4 cards that hasn't been
used in recent rounds, from a limited-size deck.
"""
    
import random
full_deck = [val for val in range(1, 14) for _ in range(4)]
recent_hands = []
def draw_unique_hand(deck, recent_hands, max_attempts=100):
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
    if len(deck) < 4:
        raise ValueError("Not enough cards in the deck to draw a hand.")

    for _ in range(max_attempts):
        hand = random.sample(full_deck, 4)  # fresh draw
        hand_tuple = tuple(sorted(hand))

        if hand_tuple in recent_hands:
            continue
        recent_hands.append(hand_tuple)
        return hand

    raise Exception("Failed to find a unique hand after max attempts.")

# 52-card deck: 1–13 repeated 4x
full_deck = [val for val in range(1, 14) for _ in range(4)]
recent_hands = []

# Example for 4 players x 3 rounds = 12 total rounds
for round_num in range(12):
    hand = draw_unique_hand(full_deck, recent_hands)
    print(f"Round {round_num+1} hand: {hand}")





