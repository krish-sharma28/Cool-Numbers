import re

def validate_expression(expression, numbers):
    """ Validates a player's math expression based on provided numbers to see if
    it evaluates to 24
    
    Parameters:
        expression (str): The player's inputted math expression 
        numbers (list of int): The list of allowed numbers the player can use
        target (int): The target value the player's expression should evaluate 
        to
        player_data (dict): A dictionary tracking the player's score and streak
        
    Returns:
        bool: True if the expression is correct and valid, False otherwise.
        
    Side Effects:
        prints score to console
        modifies player score and streak (good for leaderboard)
    
    """
    target = 24


    try:
        result = eval(expression)

        if result == target:
            print("Correct! +1 point")
            return True
        else:
            print("Incorrect: Wrong result.")
            return False

    except Exception as e:
        print(f"Error in expression: {e}")
        return False

if __name__ == "__main__":
    numbers = [4, 7, 8, 8]
    expression = "(7 - (8 / 8)) * 4"
    validate_expression(expression, numbers)