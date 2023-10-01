class Blackjack():
    """Class object used to run the Blackjack app in the console."""
    
    def __init__(self):
        self.art = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """ # Set the game art
        self.intro = "Welcome to Blackjack! The goal is to get your hand as close to 21 as you can.\nBut you can't go over, or the dealer wins. Round (1) starts now!"
        self.status = True  # Set object status to True
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    # List of cards to deal
        self.user_cards = []    # Stores dealt cards for user
        self.dealer_cards = []   # Stores dealt cards for dealer

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

    def deal_cards(self):
        """Method to randomly select a card from the deck and returns the index."""
        
        import random   # Import random module to use when 'picking' cards
        
        get_card = random.randint(1,len(self.cards) - 1) # Get random index from cards list
        
        return get_card # Return index

    def compare_scores(self):
        """Method to calculate final scores at the end of the game and determine the winner"""
        
        scores = self.get_scores() # Calls function to get updated scores for each hand

        if scores["Dealer"] < 17:   # Checks id dealer hand has less than 17
            
            self.dealer_cards.append(self.cards[self.deal_cards()])    # Pulls another card
            scores = self.get_scores()   # Updates the score
            
        dealer_score = scores["Dealer"] # Get the dealer score and set to variable
        user_score = scores["User"] # Get the user score and set to variable

        # Loops during first deal of 2 cards if check_score() triggers false
        if len(self.user_cards) == 2:
            
            # Checks if Blackjack on first round 
            if 11 in self.user_cards and 10 in self.user_cards:   # Ace and Jack/Queen/King
                
                return "User with Blackjack"    # User wins automatically
        
        if len(self.dealer_cards) == 2:
            
            # Checks if Blackjack on first round
            if 11 in self.dealer_cards and 10 in self.dealer_cards:   # Ace and Jack/Queen/King
                return "Dealer with Blackjack"  # Dealer wins automatically

        # Determines if Ace is 11 or 1
        if 11 in self.user_cards and user_score > 21:    # If over 21, Ace is 1
            user_score -= 10    # Subtracts 10 from score
            
        elif 11 in self.dealer_cards and dealer_score > 21:  # If over 21, Ace is 1
            dealer_score -= 10  # Subracts 10 from score

        if user_score > 21 and dealer_score > 21:   # If both hands are over 21
            return "Neither"    # No winner

        if user_score > 21: # If user score is over 21
            return "Dealer" # Dealer wins
        
        elif dealer_score > 21: # If dealer score is over 21
            return "User"   # User wins
        
        elif user_score == dealer_score:    # If score is the same
            return "Draw"   # Tied
        
        elif user_score > dealer_score: # If user score is greater than dealers
            return "User"   # User wins
        
        elif dealer_score > user_score: # If dealer score is greater than users
            return "Dealer" # Dealer wins

    def check_hands(self):
        """Method used to check each players hand during game play for certain conditions and determines if game continues or ends."""
       
        user_score = sum(self.user_cards)    # Checks sum of user cards
        dealer_score = sum(self.dealer_cards)    # Checks sum of dealer cards
        
        if user_score > 21 and dealer_score > 21:   # If both hands are over 21
            return True # End game

        # Loops during first deal of 2 cards
        if len(self.user_cards) == 2:
            # Checks if Blackjack on first round
            if 11 in self.user_cards and 10 in self.user_cards:
                return True    # End game
        if len(self.dealer_cards) == 2:
            # Checks if Blackjack on first round
            if 11 in self.dealer_cards and 10 in self.dealer_cards:
                return True    # End game
        
        if user_score > 21: # If user score is over 21
            return True # End game
        elif dealer_score > 21: # If dealer score is over 21
            return True # End game
        else:   # If no condition is met
            return False    # Continue game

    def get_scores(self):
        """Method used to calculate current scores for user and dealer and sets to dictionary."""
        
        user_score = sum(self.user_cards)    # Get user score
        dealer_score = sum(self.dealer_cards)    # Get dealer score
        scores = {
            "User":user_score,  # Set user score
            "Dealer":dealer_score   # Set dealer score
        }
        
        return scores   # Return the dictionary
    
    def clear_hands(self):
        """Method used to reset card lists for new game."""
        
        self.user_cards = []    # Blank list for new user hand
        self.dealer_cards = []    # Blank list for new dealer hand
    
    def print_game_menu(self):
        """Method to print main menu to the console."""
        
        self.print_game_art()  # Prints menu art
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
        
    def play(self):
        """Main method to run game script."""
        
        self.print_game_menu()

        for i in range(0,2):    # Deals first round of cards
            
            self.user_cards.append(self.cards[self.deal_cards()])  # Deal user cards, adds to user list
            self.dealer_cards.append(self.cards[self.deal_cards()])    # Deal dealer cards, add to dealer list

        while self.status: # While game is active
            
            scores = self.get_scores()   # Get initial/updated scores
            
            print("\n" + 81 * "#" + "\n#") # Print top border
            print(f"# Your cards: {self.user_cards}, current score: {scores['User']}")   # Prints cards and score for user
            print(f"# Dealer's cards: {self.dealer_cards}\n" + "#")   # Prints cards in dealer hand
            print(81 * "#") # Print bottom border

            if self.check_hands():   # Checks if conditions are met to end game
                self.status = False    # Stops loop if true
        
            else:   # If false, continue
                
                hit = input("\nType Y to get another card, N to pass: ").lower() # Check if user wants another card
                
                if hit == "n":  # If no
                
                    self.status = False    # Stop loop
                    self.compare_scores()    # Get results of game
                    scores = self.get_scores()   # Update the scores
                
                elif hit == "y":    # If yes
                    
                    self.user_cards.append(self.cards[self.deal_cards()])  # Get and add next card to users list
                    self.dealer_cards.append(self.cards[self.deal_cards()])    # Get and add next card to dealers list
        
        self.clear()    # Clear console
        self.print_game_art()   # Print game art
        print(81 * "#" + "\n#")
        print(f"# Your final hand: {self.user_cards}, final score: {scores['User']}")    # Print final cards and user score
        print(f"# Dealer final hand: {self.dealer_cards}, final score: {scores['Dealer']}\n#")    # Print final cards and dealer score
        print(81 * "#" + "\n") # Print bottom border
        
        winner = self.compare_scores()   # Compare the hands one more time for updates
        
        if winner == "Dealer":
            
            winner = """ 
                        ___           _          __      ___         _ 
                       |   \ ___ __ _| |___ _ _  \ \    / (_)_ _  __| |
                       | |) / -_) _` | / -_) '_|  \ \/\/ /| | ' \(_-<_|
                       |___/\___\__,_|_\___|_|     \_/\_/ |_|_||_/__(_)
                    """

            print(winner)
            
        elif winner == "User":
            
            winner = """
                     _   _              __      ___         _ 
                    | | | |___ ___ _ _  \ \    / (_)_ _  __| |
                    | |_| (_-</ -_) '_|  \ \/\/ /| | ' \(_-<_|
                     \___//__/\___|_|     \_/\_/ |_|_||_/__(_)
                """
            print(winner)

        start_game = input("\nDo you want to play another game of Blackjack? Y or N: ").lower() # Prompt if user wants to play again

        if start_game == "y":   # If yes

            self.clear()    # Clear the console
            self.clear_hands()  # Collect the cards
            self.play()   # Restart game
        
        else:   # If no
            return  # End game
