class Magic_8_Ball():
    """Class object used to run the Magic 8 Ball app in the console."""
    
    def __init__(self):
        
        self.art = """
         __  __             _         ___    ____        _ _ 
        |  \/  | __ _  __ _(_) ___   ( _ )  | __ )  __ _| | |
        | |\/| |/ _` |/ _` | |/ __|  / _ \  |  _ \ / _` | | |
        | |  | | (_| | (_| | | (__  | (_) | | |_) | (_| | | |
        |_|  |_|\__,_|\__, |_|\___|  \___/  |____/ \__,_|_|_|
                      |___/                                  
        """ # Set the menu art
        # Add intro line
        self.intro = (f"Welcome to Magic 8 Ball where all of your fortunes will be answered!\n"
                      f"Are you ready to ask the questions weighing on your mind?")
        self.status = True  # Set object status to True
        self.question = "Will I win the lottery?"  # Set question to answer
        self.api_response = "Not likely at this time"  # Set the response
        self.api_endpoint = "https://eightballapi.com/api"   # Set API url prefix

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
        
        print(81 * "*") # Print top border
        print(self.intro)   # Prints intro
        print(81 * "*") # Print bottom border
        print() # Blank line
        
    def get_status(self):
        """Method used to get menu status."""
        
        return self.status   # Return the menu status

    def print_main_menu(self):
        """Method to print main menu to the console."""
        
        self.print_menu_art()  # Prints menu art
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
    
    def get_question(self):
        """Method used to get user question for Magic 8 Ball api reading."""

        return self.question    # Return the question
    
    def set_question(self, question):
        """Method used to set user question for Magic 8 Ball api reading."""
        
        # Format
        self.question = str(question).replace(" ", "+").strip()

    def get_api_endpoint(self):
        """Method used to get API URL."""

        return self.api_endpoint    # Return the API endpoint url
    
    def set_api_endpoint(self, url):
        """Method used to set API URL - prefix is default, this method appends the attributes."""

        self.api_endpoint = url    # Set the API endpoint url

    def get_reading(self):
        """Method to request API data to get reading for user."""
        
        return self.api_response["reeading"]    # Return response string
        
    def reset(self):
        """Method used to reset the question for a new reading."""
        
        self.question = ""  # Clears the string
        
    def get_api_response(self):
        """Method used to request API response."""
        
        import random   # Import random to choose lucky or biased reading
        import requests # Import requests to call API data
        
        choice = random.randint(0,1)    # Set choice number
        
        if choice == 0: # If lucky reading
            
            response = requests.post(f"{self.api_endpoint}")
            self.api_response = response.json() # Set the response
            
            return self.api_response["reading"]
        
        elif choice == 1:   # If biased reading
            
            response = requests.post(f"{self.api_endpoint}/biased?question={self.question}")
            self.api_response = response.json() # Set the response
            
            return self.api_response["reading"]
        
    def play(self):
        """Method to load Magic 8 Ball game for user."""
        
        while self.status: # While menu is active
            
            self.print_main_menu()  # Print game menu for user
        
            # Prompt user to ask a question
            user_question = input(f"What would you like to ask the Magic 8 Ball?: ")
            self.set_question(user_question)    # Call method to set new question

            # Output the API response to the user
            print(self.get_api_response()+"\n")

            # Check if user wants to play again
            play_again = input("Would you like to ask another question? (Y/N): ")
                
            # If user wants to play again
            if play_again.lower() == "y":
                
                self.reset()    # Reset the game
                self.play()     # Call method to play again
                
            #If the user does not want to play again
            else:
                
                self.status = False # Ends the loop
