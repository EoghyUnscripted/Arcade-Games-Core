class Brain:

    def __init__(self, question_list):
        self.question_id = 0    # Set default ID to 0
        self.question_list = question_list
        self.score = 0      # Set default score to 0

    def still_has_questions(self):
        """Function to check if there are more questions in the list."""
        
        return self.question_id < len(self.question_list)   # Returns True or False

    def next_question(self):
        """Function to prompt next question and accept user guess if True or False."""
        
        current_question = self.question_list[self.question_id]     # Get current question
        self.question_id += 1   # Set ID so questions start at 1 instead of 0
        
        # Get user answer for the question
        guess = input(f"Q.{self.question_id}: {current_question.text} (True/False): ")
        
        self.check_answer(guess, current_question.answer)   # Check if the guess is correct

    def check_answer(self, guess, correct_answer):
        """Function to check if user guess is the correct answer."""
        
        # Check if guess matches answer, i.e. T/F or True/False input accepted
        if guess.lower() == correct_answer.lower() or guess.lower() == str(correct_answer[0]).lower():
            
            print("You got it right!")  # Print message
            self.score += 1     # Add a point to the score
            
        else:   # If wrong
            
            print("That's wrong.")  # Print message

        print(f"The correct answer was: {correct_answer}.")     # Print the correct answer
        print(f"Your current score is: {self.score}/{self.question_id}\n")      # Print current score