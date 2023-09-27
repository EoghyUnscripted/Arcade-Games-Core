import os
from Apps.Treasure_Island.Modules import treasure_island_menu as menu

def clear():
    """Function used to clear the console."""
    
    os.system('clear') #on Linux System

def load():
    """Function to load the Treasure Island program."""
    
    data = menu.get_all_stories()   # Get the data from the JSON file
    story_id = [i for i in data["adventures"]]  # Filter stories
    story_names = [data["adventures"][i]["name"] for i in story_id] # Filter story names
    options = " / ".join(story_id)  # String story numbers together to prompt user later
    
    menu.menu() # Call the menu, which is really just the art and welcome message
    
    # Ok so this gets all the options for stories
    for i in story_id:
        
        # Then it prints the list out on the screen to pick a storyline theme
        print(i + ". " + story_names[int(i)-1])
    
    # This captures the user's input and I really hope they weren't careless
    game_choice = input("\nPlease type " + options.upper() + " to choose your story: ")
    
    # So we're going to try to pass the input
    try:
        
        # Here we call the menu and pass the input
        menu.play_scenes(game_choice)
        
    # If it didn't like it, then it rejects it like so
    except KeyError:
        
        # This is another attempt to try a new number cause it was a letter last time, silly
        game_choice = input("Try a different number: ")
        menu.play_scenes(game_choice)   # Fail this time and the game dies, I don't make the rules 