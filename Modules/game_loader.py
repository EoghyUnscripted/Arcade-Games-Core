from Apps.Blackjack import blackjack
from Apps.Hangman import hangman
from Apps.Quiz_Game import quiz_game

def get_game(name):
    """ Function used to call the application load function in the chosen game. """
    
    if name == "blackjack":
        
        blackjack.load()
        
    elif name == "hangman":
        
        hangman.load()

    elif name == "quiz_game":
        
        quiz_game.load()    

def load(game):
    """ Function used to load user chosen game to the console. """
    
    try:
        
        # Check if Exit command string
        if str(game).lower() == "exit":
        
            return
        
        else:
            
            get_game(str(game).lower())
        
    except IndexError:
        """ Error handling for user input that is out of range. """
        
        # Alert user of invalid input
        print("\nSorry, that number is not an option. Please, try again.")
        game = input("Let's try one more time. Chose a number from the menu: ")
        
    except ValueError:
        """ Error handling for user input that is an integer. """
        
        # Alert user of invalid input
        print("\nSorry, you must enter a valid integer or 'EXIT' to end program. Please, try again.")
        game = input("Let's try one more time. Chose a number from the menu: ")
        
    except:
        """ Error handling catchall. """
        print("Sorry, we could not load the game at this time. Try again, later.")
        exit