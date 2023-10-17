class Hangman():
    """Class object used to run the Hangman app in the console."""
    
    def __init__(self):
        self.art =  ''' 
                 _                                             
                | |                                            
                | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
                | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                | | | | (_| | | | | (_| | | | | | | (_| | | | |
                |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |                      
                                   |___/    ''' # Set the game art
        self.intro = (f"Welcome to the classic game of Hangman! The goal is to guess the word before it's GAME OVER!\n"
                      f"Are you ready to try your luck? No cheating!")
        self.status = True  # Set object status to True
        self.lives = 6   # Variable to track lives remaining in game
        self.chosen_word = self.get_new_word()  # Blank variable to hold chosen word
        self.display = []    # Blank list to hold correct guesses
        self.guess_list = [] # Blank list to store all guesses
        self.stages = [i for i in self.get_stages()]    # Populate list with stage art

    def get_stages(self):
        """Method used to get stages art from external python file."""
        
        # Import the necessary data file
        from Classes.Data.hangman_stages import stages as lives
        
        stages = [i for i in lives] # Create new list with file data
        
        return stages   # Return list of stages artwork
       
    def get_new_word(self):
        """Method that returns a random word from the list."""
        
        import json
        import random
        
        with open("Classes/Data/hangman_words.json", "r") as file:
    
            read_file = json.load(file) # Read data to variable
            
        word_list = [i for i in read_file]  # Create new list from file data
        chosen_word = random.choice(word_list).upper() # Get a random word from the list
        
        return chosen_word
 
    def set_new_word(self, word):
        """Method that sets a chosen word."""
        
        self.chosen_word = word # Set the new word
        
    def get_game_art(self):
        """Method used to get game art."""
        
        return self.art # Returns menu art
    
    def print_game_art(self):
        """Method used to print game art to console."""
        
        print(self.art) # Prints menu art
        
    def get_intro(self):
        """Method used to get menu intro."""
        
        return self.intro   # Return the menu intro
    
    def print_intro(self):
        """Method used to print menu intro to console."""
        
        print(81 * "*")  # Prints a top border
        print(self.intro)   # Prints intro
        print(81 * "*") # Prints a bottom border
        
    def get_status(self):
        """Method used to get menu status."""
        
        return self.status   # Return the menu status

    def print_game_menu(self):
        """Method to print main menu to the console."""
        
        self.print_game_art()  # Prints menu art
        self.print_intro() # Prints intro
        
    def clear(self):
        """Method to clear the console."""
        
        import os
        import platform
        
        # Attempt to clear console
        try:
            
            # Check if Linux OS
            if platform.system().lower() == "linux":
                
                os.system('clear')  # Clear the console
            
            # Check if Mac OS
            elif platform.system().lower() == "darwin":
                
                os.system('clear')  # Clear the console
            
            # Check if Windows OS
            elif platform.system().lower() == "windows":
                
                os.system('cls')  # Clear the console
        
        # If other OS
        except:
            
            return  # Skip the command to clear, continue program
        
    def reset(self):
        """Method used to reset the object for a new game."""
        
        self.chosen_word = self.get_new_word()  # Chose a new word
        self.display = []   # Empty the display list
        self.guess_list = []   # Empty the guesses list
        self.lives = 6  # Reset lives to 6
        self.clear()    # Clear the console
        
    def play(self):
        """Method to load Hangman game for user."""
        
        self.print_game_menu()  # Print game menu to the console
        
        # For each letter in chosen word
        for char in self.chosen_word:
            
            self.display.append("_") # Add blanks to display to user for guessing

        while self.status:  # Loops program until all blanks are filled

            guesses = ' '.join(self.guess_list).upper() # Sets the current guesses made
            print(self.stages[self.lives - 1])    # Print ASCII in current stage
            print(f"\n{' '.join(self.display)}\n")  # Print the display words
            print(f"Your guesses: {guesses}")   # Print current guesses
            guess = input("\nGuess a letter: ").upper() # Get letter input from user in lowercase

            if guess in self.guess_list:    # Check if user already guessed letter
                
                # Alert the user they have already made that guess
                print(f"You have already guessed the letter \"{guess}\".")
            
            else:   # If they guess a new letter

                self.guess_list.append(guess)   # Add letter to guess list

                for position in range(len(self.chosen_word)): # Loop through each position index
                    
                    letter = self.chosen_word[position] # Get letter in random word position
                    
                    if letter == guess: # Checks if guess matches letter
                        
                        self.display[position] = guess   # Adds to display list in same position if matches
                
                if guess not in self.chosen_word:    # Checks if guess is not in word
                    
                    self.lives -= 1  # Subtract 1 life
                    
                    if self.lives == 0:    # If no lives remain
                        
                        print(self.stages[self.lives - 1])    # Print ASCII in current stage
                        print(f"\n{' '.join(self.display)}\n")  # Print the display words
                        print("\nYou lose!\n")  # Alert the user they lose
                        
                        # Check if user wants to play again
                        play_again = input("Would you like to play another game of Hangman? (Y/N): ")
                        
                        # If user wants to play again
                        if play_again.lower() == "y":
                            
                            self.reset()    # Reset the game
                            self.play()     # Call method to play again
                            
                        #If the user does not want to play again
                        else:
                            
                            self.status = False # Ends the loop
                        
                    elif self.lives > 0: # If there are still lives remaining
                        
                        # Alert the user that the letter is not in the word
                        print(f"\nThe letter \"{guess}\" is not in the word.\n")
                    
            print(f"\n{' '.join(self.display)}\n")  # Print the display words

            if "_" not in self.display:  # Checks if blanks are filled

                print("\nYou win!\n")   # Alert the user they win
                
                # Check if user wants to play again
                play_again = input("Would you like to play another game of Hangman? (Y/N): ")
                
                # If user wants to play again
                if play_again.lower() == "y":
                    
                    self.reset()    # Reset the game
                    self.play()     # Call method to play again
                    
                #If the user does not want to play again
                else:
                    
                    self.status = False # Ends the loop