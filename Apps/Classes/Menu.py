class Menu():
    """Class object used to run the Menu app in the console."""
    
    def __init__(self):
        
        # Import required classes
        from Apps.Classes.Blackjack import Blackjack
        from Apps.Classes.Hangman import Hangman
        
        self.art = """
         ____                             _                      _      
        |  _ \ ___ _ __  _ __  _   _     / \   _ __ ___ __ _  __| | ___
        | |_) / _ \ '_ \| '_ \| | | |   / _ \ | '__/ __/ _` |/ _` |/ _ \\
        |  __/  __/ | | | | | | |_| |  / ___ \| | | (_| (_| | (_| |  __/
        |_|   \___|_| |_|_| |_|\__, | /_/   \_\_|  \___\__,_|\__,_|\___|
                                |___/                                    
        """ # Set the menu art
        # Add intro line
        self.intro = "Welcome to the Penny Arcade! Please enter a number from the list to play the game\nOr 'EXIT' to end the program."
        self.status = True  # Set object status to True
        self.games = [
                        {"name":"Blackjack","dir":Blackjack},
                        {"name":"Hangman","dir":Hangman}
                    ]   # Set list of games
        self.selected_game = None # Blank variable to store chosen game to load

    def get_menu_art(self):
        """Method used to get main menu art."""
        
        return self.art # Returns menu art
    
    def print_menu_art(self):
        """Method used to print menu art to console."""
        
        print(self.art) # Prints menu art
        
    def get_intro(self):
        """Method used to get menu intro."""
        
        return self.intro   # Return the menu intro
    
    def print_intro(self):
        """Method used to print menu intro to console."""
        
        print(81 * "*")
        print(self.intro)   # Prints intro
        print(81 * "*")
        
    def get_status(self):
        """Method used to get menu status."""
        
        return self.status   # Return the menu status

    def get_all_games(self):
        """Method used to get main menu game list."""
        
        game_list = []  # Blank list for game names
        
        for i in self.games:
            
            game_list.append(i["name"])
        
        return game_list   # Return list of games
            
    def print_all_games(self):
        """Method used to print main menu game list to console."""
        
        j = 1   # Counter for numbering the games on console
        
        # Loop through the list of games
        for i in self.games:
            
            print(f"{j}. {i['name']}")  # Print a number and the name of the game
            j += 1  # Increment counter by 1
            
    def load_selected_game(self):
        """Method used to load the selected game."""
        
        # If selected game is not set, or NoneType
        if self.selected_game is None:
            
            # Attempt to set the selected game
            try:
                
                # Prompt the user for a selection
                user_choice = int(input("Sorry, can you remind us which game you chose?: "))
                self.set_selected_game(user_choice - 1) # Set the selection
            
            # The user chose an invalid integer
            except IndexError:
                
                # Prompt the user for a different selection
                user_choice = int(input("Sorry, that one is not an option. Please try another: "))
                self.set_selected_game(user_choice - 1) # Set the selection
                
            # The user did not want to chose a valid option
            except:
                
                # Alert the user of an issue and end program.
                print("We are so sorry this is not working out. Please try again, later!")
        
        # If there is a game selected
        else:
            
            choice = self.games[self.selected_game]["dir"]
            loader = choice()
            loader.play()
            
    def set_selected_game(self, game):
        """Method to set the user selected game."""
        
        self.selected_game = game   # Sets user chosen game
        
    def print_main_menu(self):
        """Method to print main menu to the console."""
        
        self.print_menu_art()  # Prints menu art
        self.print_intro() # Prints intro
        print() # Blank line
        self.print_all_games() # Print games list
        print() # Blank line

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
        
    def main(self):
        """Main method to play the game on console."""
        
        while self.status: # While menu is active
        
            self.print_main_menu()
            
            # Get user input and check if valid input as integer
            try:
                
                # Prompt user to choose a game to play
                select_game = int(input("What game would you like to play?: ")) # User input from console
                self.set_selected_game(select_game - 1)    # Set the selected game
                self.clear()

            # Error handling if integer out of index range
            except IndexError:
                
                # Prompt user to enter a new number
                select_game = int(input("Sorry, that is not an option. Please chose another number: "))
                
            # Error handling catch-all
            except:
                
                # Promt user if they want to exit
                exit_game = input("Did you want to exit the program? (Y/N): ")
                
                # If they want to exit
                if exit_game.lower() == "y":
                    
                    self.status = False 
                    return    # Exit the program
                
                # If they do not want to exit
                elif exit_game.lower() == "n":
                    
                    # Prompt user to enter a new number
                    select_game = int(input("Please choose a number to play: "))
                    
                else:
                
                    print("\n" + 30 * "/!\\")   # Print top border
                    # Print alert message for user
                    print("Sorry, we seemed to experience unexpected technical issues during your gameplay.\nThe program will now exterminate you for your part in this error, goodbye!")
                    print(30 * "\\¡/" + "\n")   # Print bottom border
                    self.status = False    # Stop the game loop
                    exit    # Exit the program
                
            self.load_selected_game()   # Loads the selected game for user
            self.clear()    # Clear the menu
            self.main() # Runs the menu again after playing a game