
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Python version of the classic Hangman game. In this assignment, you will practice strings, loops, conditionals, and user input while managing game state from start to finish.

## 📝 Tasks

### 🛠️ Build The Core Hangman Loop

#### Description
Create the main game logic that chooses a hidden word and lets the player guess letters one at a time.

#### Requirements
Completed program should:

- Randomly select one word from a predefined list of words.
- Display the word progress using underscores for unknown letters (for example: `_ _ _ _`).
- Accept a single-letter guess from the user each turn.
- Reveal all matching letter positions when a correct guess is entered.

### 🛠️ Track Attempts And Finish The Game

#### Description
Add attempt tracking and game-ending conditions so the game can determine a win or loss and report the final result.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining and update it after wrong guesses.
- End the game with a win message when the full word is guessed.
- End the game with a loss message when attempts are exhausted.
- Show the correct word when the player loses.
