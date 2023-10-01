class Rock_Paper_Scissors():
    """Class object used to run the Rock, Paper, Scissors app in the console."""
    
    def __init__(self):
        self.art = """
                _______             _______                  _______
            ---'   ____)        ---'   ____)____         ---'   ____)____
                  (_____)                 ______)                  ______)
            ROCK   (_____)      PAPER      _______)      SCISSORS__________)
                  (____)                 _______)              (____)
            ---.__(___)         ---.__________)          ---.__(___)
        """ # Set the game art
        self.intro = "Welcome to Rock, Paper, Scissors game that you literally don't need an app to play!\nSarcasm aside, you know the drill. Time to pick a move!"
        self.status = True  # Set object status to True
        self.user_choice = ""   # Set blank variable for user choice
        self.bot_choice = self.get_random_bot_choice()    # Set blank variable for bot choice
       
    def get_bot_choice(self):
        """Function that gets the bot move choice."""
        
        return self.bot_choice  # Returns bot choice
    
    def set_bot_choice(self, choice):
        """Function that sets a move choice for the bot."""
                
        # Set the choice for bot
        self.bot_choice = choice
        
    def get_random_bot_choice(self):
        """Function that sets a random move choice for the bot."""
        
        import random   # Used to pick a random choice
        
        return random.randint(0, 2)    # Set the choice for bot
        
    def get_user_choice(self):
        """Function that get the user move choice."""
        
        return self.user_choice  # Returns user choice
    
    def set_user_choice(self, choice):
        """Function that sets a move for the user."""
                
        # Set the choice for bot
        self.user_choice = choice

    def get_game_choices(self):
        """Method used to get game choices from external file."""
        
        # Import required data files
        from Classes.Data import rock_paper_scissors_art as choice
        
        choice_list = [choice.rock, choice.paper, choice.scissors]   # Set choices to a list
        
        return choice_list  # Return choices
        
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
        
        print(81 * "*" + "\n")  # Prints a top border
        print(self.intro + "\n")   # Prints intro
        print(81 * "*") # Prints a bottom border
        
    def get_status(self):
        """Method used to get menu status."""
        
        return self.status   # Return the menu status

    def print_game_menu(self):
        """Method to print main menu to the console."""
        
        self.print_game_art()  # Prints menu art
        self.print_intro() # Prints intro
        
    def compare_moves(self):
        """Method used to compare the results and declare the winner."""
        
        # Check if tied
        if self.user_choice == self.bot_choice:
            
            print("\nIt's a tie!")  # Alert user of the tie

        # If not tied
        if self.user_choice == 0:
            
            if self.bot_choice == 1:
                
                print("Paper covers rock, you lose!")
                
            elif self.bot_choice == 2:
                
                print("Rock breaks scissors, you win!")
                
        elif self.user_choice == 1:
            
            if self.bot_choice == 0:
                
                print("Paper covers rock, you win!")
                
            elif self.bot_choice == 2:
                
                print("Scissors cut paper, you lose!")
                
        elif self.user_choice == 2:
            
            if self.bot_choice == 0:
                
                print("Rock beats scissors, you lose!")
                
            elif self.bot_choice == 1:
                
                print("Scissors cut paper, you win!")
        
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
        
        self.user_choice = ""   # Resets the user choice
        self.bot_choice = ""    # Resets the bot choice
        
    def play(self):
        """Function to load Rock, Paper, Scissors game for user."""
        
        art = self.get_game_choices()   # Sets list of game choices from file
        text = ["Rock", "Paper", "Scissors"]    # Sets printable name options
        
        while self.status:  # While game is active
        
            self.print_game_menu()  # Print game menu to the console
            
            # Attempt to get valid user input for game choice
            try:
                
                # Prompt the user to enter an integer to chose move
                self.user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
                self.bot_choice = self.get_random_bot_choice()  # Set random choice for bot
                
            # If not an integer or out of index range
            except IndexError:
                
                # Alert the user they lose
                print("That is an invalid choice, you lose!")
                self.status = False  # End the loop

            # Output the choices
            print(f"\nYou picked {text[self.user_choice]}:\n{art[self.user_choice]}\n")
            print(f"\nComputer picked {text[self.bot_choice]}:\n{art[self.bot_choice]}\n")
            
            self.compare_moves()    # Check moves for results
            
            # Prompt if user wants to play again
            play_again = input("\nDo you want to play another game of Rock, Paper, Scissors? Y or N: ").lower()
            
            # If user wants to play again
            if play_again == "y":
                
                self.clear()    # Clear the console
                self.reset()    # Reset the game for another round
                self.play()     # Restart game
                
            # If user does not want to play again
            else:
                
                self.status = False# End the loop
