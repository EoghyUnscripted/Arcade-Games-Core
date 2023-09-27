import json
from Apps.Treasure_Island.Modules import treasure_island_art as gen


def get_all_stories():
    """Function used to get stories list for users to choose for gameplay."""
    
    file = open("Apps/Treasure_Island/Data/stories.json", "r")    # Open data file to load words
    read_file = json.load(file) # Load words to variable
    
    # Return to treasure_island.py 12
    return read_file

def get_story(story_id):
    """Function used to get user chosen story for gameplay."""
    
    file = open("Apps/Treasure_Island/Data/stories.json", "r")    # Open data file to load words
    read_file = json.load(file) # Load words to variable
    story = read_file[0]["adventures"][story_id]  # Filter story
    
    return story
    
def play_scenes(story):
    """Function used to get selected story data from JSON file."""
    
    data = get_all_stories()    # Get the story data from JSON file
    story = data["adventures"][str(story).lower()]["scenes"]    # Filter scenes by selected story
    scene_count = 1 # Initial scene
    roleplay = True # Keep the game looping
    
    # Loop through scenes of selected story
    while roleplay:
        
        # Error handling
        try:
    
            # If there are more scenes to play
            if scene_count <= len(story):
                
                # Get the next scene
                lines = [i for i in story[str(scene_count)]["lines"]]
                
                print("\n", 100 * "#" + "\n", 5 * "#")  # Print top border
                
                # Loop through lines list to print
                for i in lines:
                    print(5 * "#", i)   # Print lines
                    
                print(5 * "#" + "\n", 100 * "#" + "\n") # Print bottom border
            
            # Assume the user got all the answers right
            else:
                
                # Alert them that they have won
                print('''
                        __   _____  _   _  __        _____ _   _ _ 
                        \ \ / / _ \| | | | \ \      / /_ _| \ | | |
                         \ V / | | | | | |  \ \ /\ / / | ||  \| | |
                          | || |_| | |_| |   \ V  V /  | || |\  |_|
                          |_| \___/ \___/     \_/\_/  |___|_| \_(_)
                        
                        '''
                    )
                
                # Abruptly end the game, please, and thank you
                roleplay = False
        
        except:
            "Function used as a catchall error handler."
            
            # Alert the user about a vague issue
            print("Sorry, there was an error. The game will now close.")
            roleplay = False    # End the gane as well, for good measure
            exit    # Probably overkill
        
        try:
            
            options = ""    # It's blank so I can change this, later cause mutables or whatever
            
            # Check if there are any options this scene
            if len(story[str(scene_count)]["options"]) >= 0:
                
                print("\n", 100 * "?", "\n", 5 * "?")   # Print a top border
            
                # Loop through the options list to tell the users
                for i in story[str(scene_count)]["options"]:
                    
                    print(5 * "?", story[str(scene_count)]["options"][str(i)])  # Prints the option
                    options = " / ".join(story[str(scene_count)]["options"])    # Adds option to a string
                    
                print(5 * "?", "\n", 100 * "?") # Print a bottom border
                
                choice = input("\nType " + options + " to move on: ")   # Get the user to enter an option
                
                # If the user gave the right answer, this one will run
                if choice.lower() == story[str(scene_count)]["answer"]:
                    
                    print("\n", 100 * "#" + "\n", 5 * "#")  # And they get another top border
                    
                    # Now we cycle through the lines in the message response
                    for x in story[str(scene_count)]["message"][choice]:
                    
                        print(5 * "#", x)   # And now we print all the lines
                        
                    print(5 * "#" + "\n", 100 * "#" + "\n") # And another bottom border
                    
                    scene_count += 1    # NEXT SCENE!!

                # But sometimes we type whatever we want so this checks if it's a choice or not, just in case
                elif choice.lower() in story[str(scene_count)]["message"]:
                    
                    print("\n", 100 * "#" + "\n", 5 * "#")  # Why do I even need this top border?
                    
                    # And here is where I loop through the message elements to get my lines
                    for x in story[str(scene_count)]["message"][choice]:
                    
                        print(5 * "#", x)   # And they print here so I don't even need to remember them

                    print(5 * "#" + "\n", 100 * "#" + "\n") # And again with the bottom border...
                                            
                    print(gen.gameOver) # Rude                      
                    roleplay = False    # Was it something I said?
                    
                else:
                    
                    # And lastly, just game over <3
                    print(gen.gameOver) # Well, first that silly game over thing                  
                    roleplay = False    # Then game over <3
            
        except KeyError:
            """Function used to handle KeyError. This should only happen where there are no options listed for the scene."""
            
            scene_count += 1    # NEXT SCENE!!

def menu():
    """Function used to create the main menu for users to chose their storyline."""
    
    print(gen.media_art)    # Prints menu art
    print("Welcome to Treasure Island! To start, choose a story and get your crew!\n")  # And a welcome message, too! Neat! :D