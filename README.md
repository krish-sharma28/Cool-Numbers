# Cool-Numbers

## 1. An explanation of the purpose of each file in the repository:
### - main.py: This file is the main controller for a command-line version of the 24 Game.  By running it, players can choose to play the game, view leaderboards, read game rules, or exit the game.
### - creation_and_rounds_mode.py: Defines the logic for the "Rounds" mode and include a class called Creation that creates a 4-card hand. The main capabilites of this file is to allow players play the "Rounds" mode and generate 4-card hands that could be also used in "Timed" mode.
### - expression_validator.py: This file validates players' math expression based on provided numbers to see if it evaluates to 24. 
### - helpstring.txt: ????
### - leaderboard.py: Updates and displays a leaderboard by adding a new player's score.
### - leaderboard_rounds.txt: Records players' scores who played the "Rounds" mode.
### - leaderboard_timed.txt: Records players' scores who played the "Timed" mode.
### - timed_mode.py:  Runs the timed game mode where the player has 90 seconds to solve as many hands as possible.
## 2. How to run the program: 
### Open the terminal, navigate to the folder containing the files, and run: python main.py

## 3. How to use the program: 
### When the program starts, you'll see a welcome message followed by introduction. After read through all the words, you'll see a prompt like this: What would you like to do?

### You can type one of the following options (case-insensitive):
#### - play: Starts a new game.

#### - rules: Displays how the game works and optionally opens a video tutorial.

#### - leaderboard:Show a list of top winners.

#### - exit: Quits the program.

### If you type anything other than those four keywords, you’ll get an error message prompting you to try again.

### When playing the game: 
#### 1. After typing "play", you'll be prompted to enter all player names. Enter each name followed by pressing Enter. When finished, type done.
#### 2. You'll then enter the number of rounds you'd like to play (e.g., 5).
#### 3. A random set of four numbers (a "card") will be displayed. 
#### 4. The first player who solves it types their name.
#### 5. That player is then asked to input a solution using ______?????(required input format)
#### 6. The program will use the ___??? function to check if your solution is correct or not. If the input is evaluated to exactly 24, the player earns points. Otherwise, no point is awarded. Also, the player can type "skip" if no one solves the round. 
#### 7. After all rounds are completed, the final scores for each player will be displayed.

## 4. Annotated Bibliograph:
#### 24 game How to play. (n.d.). Vimeo. https://vimeo.com/1013357391 McLeod, J. (2024, April 10). 
#### Twenty-Four - card game rules. https://www.pagat.com/adders/24.html

## 5. Attribution

| Method/Function    | Primary Author |     Techniques demonstrated       |
| -------------------|:--------------:| ---------------------------------:|
| update_leaderboard |     Krish      |     use of a key function         |
| show_leaderboard   |     Krish      |      with statements              |
| timed_mode         |     Krish      |  f-strings containing expressions |
|validate_expression |     Regan      |              regex                |