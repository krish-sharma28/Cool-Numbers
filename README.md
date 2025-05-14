# Cool-Numbers

## 1. An explanation of the purpose of each file in the repository:
### - main.py: This file is the main controller for a command-line version of the 24 Game.  By running it, players can choose to play the game, view leaderboards, read game rules, or exit the game.
### - creation_and_rounds_mode.py: Defines the logic for the "Rounds" mode and include a class called Creation that creates a 4-card hand. The main capabilites of this file is to allow players play the "Rounds" mode and generate 4-card hands that could be also used in "Timed" mode.
### - expression_validator.py: This file validates players' math expression based on provided numbers to see if it evaluates to 24. 
### - helpstring.txt: Holds the text displayed by help().
### - leaderboard.py: Updates and displays a leaderboard by adding a new player's score.
### - leaderboard_rounds.txt: Records players' scores who played the "Rounds" mode.
### - leaderboard_timed.txt: Records players' scores who played the "Timed" mode.
### - timed_mode.py:  Runs the timed game mode where the player has 90 seconds to solve as many hands as possible.
## 2. How to run the program: 
### Open the terminal, navigate to the folder containing the files, and run: python main.py
There are also optional arguments when running the program. 
***--mode*** which takes you directly to Timed or Rounds mode
***--leaderboard*** which takes you directly to Timed or Rounds leaderboard
Both take options Timed and Rounds.
e.x. ```python3 main.py --mode timed``` takes you directly to the setup for the timed mode. Helpful for debugging or just skipping beginning.
## 3. How to use the program: 
### When the program starts, you'll see a welcome message followed by introduction. After read through all the words, you'll see a prompt like this: What would you like to do?

### You can type one of the following options (case-insensitive):
#### - play: Starts a new game.

#### - rules: Displays how the game works and optionally opens a video tutorial.

#### - leaderboard:Show a list of top winners.

#### - exit: Quits the program.

### If you type anything other than those four keywords, you’ll get an error message prompting you to try again.

### When playing the game: 
#### 1. After typing "play", you'll be prompted to choose your mode ("Rounds" or "Timed"). Then you will be prompted to enter all player names. Enter each name followed by pressing Enter. When finished, type done. Note: Timed mode is always single-player, Rounds can be either
#### 2. In Rounds mode, you'll then enter the number of rounds you'd like to play (e.g., 5)., in Timed mode, your game begins once the player name is input.
#### 3. A random set of four numbers (a "card") will be displayed. 
#### 4. In rounds mode, the player will be asked to input a name. That player is then asked to input a solution. The program will use the validate_expression function to check if your solution is correct or not. If the input is evaluated to exactly 24, the player earns points. Otherwise, no point is awarded. There is an option for a "hint," and you get one per round. Also, the player can type "skip" if no one solves the round. 
#### 5. In timed mode, the player will have 90 seconds to answer as many "cards" as they can. There are no hints, but the player has an option to "skip" to the next card during rounds.
#### 6. Final scores are displayed at the end, either once the rounds have been played or once time is up.

## 4. Annotated Bibliograph:
#### 24 game How to play. (n.d.). Vimeo. https://vimeo.com/1013357391 McLeod, J. (2024, April 10). 
#### Twenty-Four - card game rules. https://www.pagat.com/adders/24.html

## 5. Attribution

| Method/Function    | Primary Author |     Techniques demonstrated       |
| -------------------|:--------------:| ---------------------------------:|
| update_leaderboard |     Krish      |     use of a key function         |
| show_leaderboard   |     Krish      |      with statements              |
| timed_mode         |     Krish      |                                   |
| validate_expression|     Regan      |     regex, list comphrehensions   |
|  generate_hint     |     Regan      |                                   |
|     get_args       |    Jordan B.   |        argument parsing           |
|       intro        |    Jordan B.   |                                   |
|       help         |    Jordan B.   |      conditional expressions      |
|     play_game      |       Jin      |            f-strings              |
|       card         |       Jin      |                                   |
|  draw_unique_hand  |       Jin      |optional parameters with default value|
                                                                 
