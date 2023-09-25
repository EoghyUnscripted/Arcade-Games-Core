import random
import json
from Apps.Hangman.Modules import hangman_art as gen

def get_new_word():
    """Function that returns a random word from the list."""
    
    file = open("Apps/Hangman/Data/hangman_words.json", "r")    # Open data file to load words
    read_file = json.load(file)
    word_list = [i for i in read_file]
    chosen_word = random.choice(word_list).upper() # Get a random word from the list
    
    return chosen_word

def load():
    """Function to load hangman game for user."""
    
    lives = 6   # Variable to track lives remaining in game
    display = []    # Blank list to hold correct guesses
    guess_list = [] # Blank list to store all guesses

    print(gen.menu_art)    # Print Logo at start of game

    play_game = True # Sets initial condition for game status
    chosen_word = get_new_word()
    
    print("test")
    
    for char in chosen_word:
        display.append("_") # Add blanks to display to user for guessing

    while play_game:  # Loops program until all blanks are filled

        guesses = ' '.join(guess_list).upper()
        print(gen.stages[lives])    # Print ASCII in current stage
        print(f"\n{' '.join(display)}\n")
        print(f"Your guesses: {guesses}")
        guess = input("\nGuess a letter: ").upper() # Get letter input from user in lowercase

        if guess in guess_list:    # Check if user already guessed letter
            print(f"You have already guessed the letter \"{guess}\".")
        else:

            guess_list.append(guess)   # Add letter to guess list

            for position in range(len(chosen_word)): # Loop through each position index
                letter = chosen_word[position] # Get letter in random word position
                if letter == guess: # Checks if guess matches letter
                    display[position] = guess   # Adds to display list in same position if matches
            
            if guess not in chosen_word:    # Checks if guess is not in word
                lives -= 1  # Subtract 1 life
                if lives == 0:    # If no lives remain
                    play_game = False  # Set end of game as False
                    print(gen.stages[lives])    # Print ASCII in current stage
                    print(f"\n{' '.join(display)}\n")
                    print("\nYou lose!\n")
                    exit()  # Stop program
                elif lives > 0: # If there are still lives remaining
                    print(f"\nThe letter \"{guess}\" is not in the word.\n")
                
        print(f"\n{' '.join(display)}\n")

        if "_" not in display:  # Checks if blanks are filled
            play_game = False  # Set end of game as False
            print("\nYou win!\n")
            
    return False