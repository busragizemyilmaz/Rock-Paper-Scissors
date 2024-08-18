# Rock-Paper-Scissors Game

## Project Goals

In designing this project, I aimed to apply fundamental Python concepts and enhance my coding skills. This project focuses on using loops, conditional statements and user input. Additionally, it helps me improve logical thinking.

## Project Overview

1. **Function Definition**
   - I created a function for the Rock-Paper-Scissors game and named it `rock_paper_scissors_YOUR_FIRSTNAME_YOUR_LASTNAME`.
   - Ensured that the function works seamlessly and can be run via the Python terminal with `rock_paper_scissors_YOUR_FIRSTNAME_YOUR_LASTNAME()`.

2. **Game Structure**
   - The game consists of multiple rounds and the player who wins the first two rounds is declared the winner.
   - After each game, both the user and the computer will be asked if they want to play another game. If both agree, the game will restart.

## Steps to Follow While Creating the Project

1. **Game Introduction**
   - I created a welcome message explaining the game rules.
   - Informed the user about how to play the game or how to exit.
   - The game should have three possible outcomes: Player wins, computer wins, or a tie.

2. **Game Setup**
   - Defined a list containing the options: Rock, Paper, and Scissors.
   - Initialized counters for the number of games played, rounds played, player wins, and computer wins.

3. **Main Game Loop**
   - Used a `while` loop to make the game playable.
   - Reset round and win counters for each new game.

4. **Rounds Loop**
   - Used another `while` loop to keep playing rounds until a player or computer wins two rounds.
   - Prompted the user to make a choice from the three options and asked them to choose again if an invalid option was selected.
   - Generated the computer’s choice randomly.
   - Used logical operations or basic `if-else` statements to determine the winner of each round.
   - Updated the win counters based on who won the first two rounds.
   - Printed the result of each round to the screen.

5. **Determining the Game Winner**
   - After the rounds loop ends (when a player wins two rounds), determined the overall winner of the game and displayed the appropriate message.

6. **Continuation Request**
   - Asked the user if they wanted to play another game.
   - Asked if the computer wanted to continue playing (created a random response for this).
   - If both parties agree to continue, the game will continue; if either party does not want to continue, the game will end.
   - Displayed appropriate messages for each situation.


