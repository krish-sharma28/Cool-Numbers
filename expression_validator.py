import re

def validate_expression(expression, numbers, target, player_data):

    
    used_numbers = list(map(int, re.findall(r'\d+', expression)))

    
    temp_numbers = numbers.copy()
    for num in used_numbers:
        if num in temp_numbers:
            temp_numbers.remove(num)
        else:
            print("Incorrect: Used invalid numbers.")
            player_data['streak'] = 0
            return False

    try:
        result = eval(expression)

        if result == target:
            print("Correct!")
            player_data['score'] += 10
            player_data['streak'] += 1
            return True
        else:
            print("Incorrect: Wrong result.")
            player_data['streak'] = 0
            return False

    except Exception as e:
        print(f"Error in expression: {e}")
        player_data['streak'] = 0
        return False

if __name__ == "__main__":
    
    numbers = [4, 7, 8, 8]
    target = 24
    expression = (7-(8/8))*4

    player_data = {'score': 0, 'streak': 0}

    validate_expression(expression, numbers, target, player_data)
    print(player_data)