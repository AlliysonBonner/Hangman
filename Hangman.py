# Hangman
# This is a game for in which one player tries to guess the letters of a word, and
# failed attempts are recorded by drawing a gallows and someone hanging on it,
# line by line.


# Author: Alliyson Bonner
# Github: https://github.com/alliysonbonner
# Linkedin: https://www.linkedin.com/in/alliyson
# Email: alliyson.bonner@gmail.com
# Date: December 09 2022

# import libraries
import random
import string
from words import words

def get_valid_word(words):
  """Select a word from a list of words that does not contain any space or dashes,
  randomly. Ensure all letters of the selected word are uppercase.
  
  Args:
  	words(list): A list of words.
    
  Returns(str):
  	A random uppercase word with no dashes or spaces.
  """
  word = random.choice(words)
  while '-' in word or ' 'in word: 
    word = random.choice(words)
    
  return word.upper()

def hangman():
  """hangman starts and manages a game of hangman."""
  # Define word, word_letters, alphabet, and used_letters. Word gets words without dashes
  # or spaces from the list of words. word_letters stores each unique letter in the word 
  # that has not been guessed. alphabet has each uppercase letter of the alphabet. 
  # used_letters holds all guessed letters
  word = get_valid_word(words)
  word_letters = set(word) #we only want each letter 1 time
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  
  lives = 6
  
  while len(word_letters) > 0 and lives > 0:
    # Tell the user how many lives there are for the duration of the game and what 
    # letters have already been used.
    print('You have', lives, 'lives left and you used these letters: ', ' '.join(used_letters))
    
    # Display the current word to the user, replacing unguessed letters with '-'.
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))
    
  	# Get the user input
    user_letter = input('Guess a letter: ').upper()
    
    # Check if user made an appropriate guess. If user's guess is appropiate add it
    # to used_letters. If user guess is correct remove it from word_letters. 
    # Otherwise subtract a life
    # alphabet = {'A', 'B', 'C' ...} 
    # used_letters = {'C', 'T', 'B'}
    # alphabet - used_letters = {'A', 'D', 'E' ... 'S', 'U', ...}
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
          word_letters.remove(user_letter)
      else:
        lives -= 1

    # Tell user to pick a new letter because they have already used the one they picked.
    elif user_letter in used_letters:
      print('You have already used that character. Please try again.')

    # Tell user to enter an alphabet charater.
    else:
      print('Ivalid character. Please try again.')
  
  # Tell user if they won or lost
  if lives == 0:
    print('You died, sorry. The word was', word)
  else:
 	 print('You guessed the word', word, '!!')

if __name__ == "__main__":
  hangman()