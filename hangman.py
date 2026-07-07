"""
CodeAlpha - Python Programming Internship
Task 1: Hangman Game

A simple text-based Hangman game.
- Player guesses a word one letter at a time.
- 6 incorrect guesses allowed.
- Console-based input/output only.

Key concepts used: random, while loop, if-else, strings, lists.
"""

import random

# A small predefined list of words to choose from
WORDS = ["python", "hangman", "developer", "internship", "keyboard"]

MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly select a word from the list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def draw_hangman(incorrect_guesses):
    """Return a simple ASCII hangman drawing based on incorrect guesses so far."""
    stages = [
        """
           --------
           |      |
           |
           |
           |
           |
        ---------
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        ---------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |
           |
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |
           |
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
        ---------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        ---------
        """,
    ]
    return stages[incorrect_guesses]


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("       WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(draw_hangman(incorrect_guesses))
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word: " + word)
            break

        guess = input("\nGuess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.\n")

    else:
        # This runs if the while loop exits because incorrect_guesses reached the max
        print(draw_hangman(incorrect_guesses))
        print(f"\n💀 Game Over! You've run out of guesses. The word was: {word}")

    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again == "y":
        print("\n")
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye. 👋")


if __name__ == "__main__":
    play_hangman()