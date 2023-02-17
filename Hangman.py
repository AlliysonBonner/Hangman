import random
import string
from words import words

def get_valid_word(words):
    """
    Select a word from a list of words that does not contain any spaces or dashes, randomly. Ensure all letters of
    the selected word are uppercase.

    Args:
        words (list): A list of words.

    Returns:
        str: A random uppercase word with no dashes or spaces.
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    """
    This function starts and manages a game of hangman.
    """
    word = get_valid_word(words)
    word_letters = set(word)  # A set of the unique letters in the word
    alphabet = set(string.ascii_uppercase)  # A set of uppercase letters of the alphabet
    used_letters = set()  # A set of letters the user has guessed
    lives = 6  # The number of lives the user has

    while len(word_letters) > 0 and lives > 0:
        # Display the number of lives remaining and the letters the user has guessed
        print(f"You have {lives} lives left and you've used these letters: {' '.join(used_letters)}")

        # Display the current word to the user, replacing unguessed letters with '-'
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            # If the user's guess is valid, add it to used_letters
            used_letters.add(user_letter)

            if user_letter in word_letters:
                # If the user's guess is in the word, remove it from word_letters
                word_letters.remove(user_letter)
            else:
                # If the user's guess is not in the word, subtract a life
                lives -= 1
        elif user_letter in used_letters:
            # If the user has already guessed the letter, ask them to pick another one
            print("You've already used that letter. Please try again.")
        else:
            # If the user's guess is not a valid letter, ask them to try again
            print("Invalid character. Please try again.")

    # The game is over: either the user has won or lost
    if lives == 0:
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"Congratulations! You guessed the word {word}!!")


if __name__ == "__main__":
    hangman()
