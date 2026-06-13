# Game - https://appbrewery.github.io/python-day7-demo/

import random
from hangman_wordlist import word_list

stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]

word_list = ["baboon", "camel", "sunday", "monday", "delivery"]

# Choose a random word
chosen_word = random.choice(word_list)

# Uncomment the next line while testing
# print(chosen_word)

word_length = len(chosen_word)

lives = 6
game_over = False

# Create placeholder
display = []

for _ in range(word_length):
    display.append("-")

print("Welcome to Hangman!")
print(" ".join(display))

correct_letters = []

while not game_over:

    guess = input("\nGuess a letter: ").lower()

    # Check for repeated guess
    if guess in correct_letters:
        print(f"You already guessed '{guess}'.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

            if guess not in correct_letters:
                correct_letters.append(guess)

    # Wrong guess
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("\nYou Lose!")
            print(f"The word was: {chosen_word}")

    # Display current progress
    print("\nCurrent word:")
    print(" ".join(display))

    # Display hangman stage
    print(stages[6 - lives])

    print(f"Lives remaining: {lives}")

    # Check if player won
    if "-" not in display:
        game_over = True
        print("\n🎉 Congratulations! You Win!")