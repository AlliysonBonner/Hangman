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
  word = random.choice(words)
  while '-' in word or ' 'in word: 
    word = random.choice(words)
    
  return word.upper()

def hangman():
  # TODO: Describe the next 4 lines.
  word = get_valid_word(words)
  word_letters = set(word) #we only want each letter 1 time
  alphabet = set(string.ascii_uppercase)
  used_letters = set()
  
  lives = 6
  
  # Get the user input
  while len(word_letters) > 0 and lives > 0:
    # TODO: Add comments
    # TODO: Add comments
    print('You have', lives, 'lives left and you used these letters: ', ' '.join(used_letters))
    
    # TODO: Add comments
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))
    
    user_letter = input('Guess a letter: ').upper()

    # TODO: Describe the next 4 lines.
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      if user_letter in word_letters:
          word_letters.remove(user_letter)
          
      else:
        lives -= 1

    # TODO: Describe the next 2 lines.
    elif user_letter in used_letters:
      print('You have already used that character. Please try again.')

    # TODO: Describe the next 2 lines.
    else:
      print('Ivalid character. Please try again.')
  
  if lives == 0:
    print('You died, sorry. The word was', word)
  else:
 	 print('You guessed the word', word, '!!')
  
  
if __name__ == "__main__":
  hangman()