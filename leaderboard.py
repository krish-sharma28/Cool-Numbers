def update_leaderboard(player_name, score, file_path='leaderboard.txt'):
    """
    Updates and displays a leaderboard by adding a new player's score.

    Parameters:
    - player_name (str): The name of the player submitting a score.
    - score (int): The player's score to be added to the leaderboard.
    - file_path (str): Optional. The path to the leaderboard text file. 
        Defaults to 'leaderboard.txt'.

    Side effects:
    - Modifies the leaderboard file to include the new score.
    - Prints the updated leaderboard to the console.
    """
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f"{player_name},{score}\n")

    scores = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            name, points = line.strip().split(',')
            scores.append((name, int(points)))

    scores.sort(key=lambda x: x[1], reverse=True)

    print("\n--- Leaderboard ---")
    i = 0
    while i < len(scores):
        name = scores[i][0]
        points = scores[i][1]
        print(str(i + 1) + ". " + name + " - " + str(points) + " points")
        i = i + 1

