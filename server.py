import os
from Modules import menu, game_loader as loader

end_of_game = False # Start gameplay Loop

def clear():
    """Function used to clear the console."""
    os.system('clear') #on Linux System

while not end_of_game:
    
    # Get game name from users choice
    try:
        
        # clear()
        game_to_play = menu.load_menu()    # Call menu
        
        # Check if user wants to end game
        if game_to_play == False:
            
            end_of_game = True  # Set end of game to true
        
        # Load user game choice
        else:
            
            loader.load(game_to_play)   # Call new instance of game for User
        
    except IndexError:
        """Error handling for user input that is out of range."""
        
        # Alert user of invalid input
        print("\nSorry, that number is not an option. Please, try again.")
        
    except ValueError:
        """Error handling for user input that is not an integer."""
        
        # Alert user of invalid input
        print("\nSorry, you must enter an integer or 'EXIT' to end program. Please, try again.")