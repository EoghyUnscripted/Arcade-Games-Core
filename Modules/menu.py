import json
from Modules import menu_art as gen, game_loader as game

def get_menu():
    """Function used to get main menu list and print to console."""
    
    file = open("Data/menu.json", "r")  # Call JSON file and read the contents
    
    menu_file = json.load(file) # Load variable with JSON data
    
    menu_output = [menu_file[0][i]["name"] for i in menu_file[0]] # Create a menu of games
    
    art = get_menu_art()    # Get menu art to display in console
    
    menu = [art, menu_output] # Create a hash table to return data
    
    return menu

def get_menu_art():
    """Function used to get random main menu art and print to console."""
    
    art = gen.create_art(gen.styles_list)
    
    return art

def load_menu():
    """Function used to get and print art and menu to console."""

    new_menu = get_menu()   # Get a new menu
    j = 1   # Counter for menu loop
    
    print(new_menu[0])  # Print menu art to console
    
    print(f"{'#' * 50}\n{'#' * 50}\n"
            + f"\n{' ' * 20}Main Menu\n")   # Print top banner

    # Print all menu items
    for i in range(0, len(new_menu[1])):
        output = f"{j}  {new_menu[1][i]}"
        print(output)
        j += 1

    print(f"\n{'#' * 50}\n{'#' * 50}")
    
    try:
    
        # Get user input for game selection
        game_choice = int(input("\nEnter the number to play the game. What is your choice? "))
        
        user_choice = str(new_menu[1][game_choice - 1]).lower()
            
        return user_choice

    except IndexError:
        """Error handling for user input that is out of range."""
        
        # Alert user of invalid input
        print("\nSorry, that number is not an option. Please, try again.")
        
    except ValueError:
        """Error handling for user input that is not an integer."""
        
        game_choice = input("Did you want to exit the game? (Y or N) ")
        
        if str(game_choice).lower() == "y" or str(game_choice).lower() == "yes":
            
            return False
        
        elif str(game_choice).lower() == "n" or str(game_choice).lower() == "no":
            
            return True
            
        else:
        
            # Alert user of invalid input
            print("\nSorry, you must enter an integer or 'EXIT' to end program. Please, try again.")
        
