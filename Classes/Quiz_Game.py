class Quiz_Game():
    """Class object used to run the Quiz Game app in the console."""
    
    def __init__(self):
        
        self.art = """
          ___        _        ____                      _ 
        /  _  \_   _(_)____ /  ___| __ _ _ __ ___   ___| |
        | | | | | | | |_  / | |  _ / _` | '_ ` _ \ / _ \ |
        | |_| | |_| | |/ /  | |_| | (_| | | | | | |  __/_|
        \____\_\\__,_|_/___| \_____|\__,_|_| |_| |_|\___(_)
        """ # Set the menu art
        # Add intro line
        self.intro = (f"Welcome to the Quiz Game! Let's test your trivia knowledge.\n"
                      f"Do you think you have what it takes to win?")
        self.status = True  # Set object status to True
        self.question_bank = self.get_question_bank() # Populates a list with questions
        self.score = 0  # Variable to set the game score

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
    
    def get_question_bank(self):
        """Method used to populate question list for gameplay."""
        
        # Import the required modules
        from Classes.Data import quiz_game_questions as data
        from Classes.Modules.Quiz_Game_Question import Question
        
        question_list = []  # Blank list for new question list
        
        # Loop through question list
        for row in data.get_question_list():
            question_text = row["text"]     # Get questions
            question_answer = row["answer"]     # Get answers
            # Create new question object for each question in list
            new_question = Question(question_text, question_answer)
            question_list.append(new_question)  # Append to question list

        return question_list    # Return the question list
    
    def set_question_bank(self):
        """Method used to populate question list for gameplay."""
        
        # Import the required modules
        from Classes.Data import quiz_game_questions as data
        from Classes.Modules.Quiz_Game_Question import Question
        
        # Loop through question list
        for row in data.get_question_list():
            question_text = row["text"]     # Get questions
            question_answer = row["answer"]     # Get answers
            # Create new question object for each question in list
            new_question = Question(question_text, question_answer)
            self.question_bank.append(new_question)  # Append to question bank list

    def reset(self):
        """Method used to reset the object for a new game."""
        
        # Repopulate list with new questions
        self.question_bank = self.get_question_bank()
        
    def play(self):
        """Method to load Quiz Game for user."""
        
        # Import required classes
        from Classes.Modules.Quiz_Game_Brain import Brain
        
        while self.status: # While menu is active
        
            self.print_main_menu()  # Print game menu for user

            quiz = Brain(self.question_bank)  # Create new quiz object

            while quiz.still_has_questions():   # Loop through questions
                
                quiz.next_question()    # Get next question

            final_score = quiz.score    # Get final score
            final_percent = (quiz.score / len(quiz.question_list))*100  # Get final score percent
            final_percent = int(final_percent)  # Convert percent to integer

            # Output the final results of the quiz
            print(f"You've completed the quiz.\n"
                f"Your final score is: {final_score}/{len(quiz.question_list)} or {final_percent}%.")

            # Check if user wants to play again
            play_again = input("Would you like to play another round of Quiz Game? (Y/N): ")
                
            # If user wants to play again
            if play_again.lower() == "y":
                
                self.reset()    # Reset the game
                self.play()     # Call method to play again
                
            #If the user does not want to play again
            else:
                
                self.status = False # Ends the loop