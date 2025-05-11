def update_leaderboard(player_name, score, mode):
    """
    Updates and displays a leaderboard by adding a new player's score.

    Parameters:
    - player_name (str): The name of the player submitting a score.
    - score (int): The player's score to be added to the leaderboard.
    - mode (str): The game mode ('timed' or 'rounds') to 
        select the correct leaderboard file.

    Side effects:
    - Modifies the leaderboard file to include the new score and makes sure
        the scores are sorted.
    """
    file_path = f"leaderboard_{mode}.txt"
    scores = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            name, points = line.strip().split(',')
            scores.append((name, int(points)))

    scores.append((player_name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        for name, points in scores:
            f.write(f"{name},{points}\n")
    
def show_leaderboard(mode):
    """
    Displays the leaderboard for the specified game mode.

    Parameters:
    - mode (str): The game mode ('timed' or 'rounds') to
        select the correct leaderboard file.

    Side effects:
    - Prints the leaderboard to the console.
    """
    filename = f"leaderboard_{mode}.txt"
    with open(filename, 'r', encoding='utf-8') as f:
        print(f"\n--- {mode.capitalize()} Mode Leaderboard ---")
        scores = []
        for line in f:
            name, points = line.strip().split(',')
            scores.append((name, int(points)))

        i = 0
        while i < len(scores):
            name = scores[i][0]
            points = scores[i][1]
            print(str(i + 1) + ". " + name + " - " + str(points) + " points")
            i += 1
   
