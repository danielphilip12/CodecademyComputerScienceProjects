import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def player_choice(self):
        while True:
            player_choice = input("Choose rock, paper, or scissors: ")
            if player_choice in self.choices:
                break
            print("That option is not available. Spelling does matter")

        return player_choice

    def computer_choice(self):
        return random.choice(self.choices)
    
    def determine_winner_or_tie(self, player, computer):
        if player == computer:
            return "It's a tie"

        if player == "rock":
            if computer == "scissors":
                return "You win"
            else:
                return "You lose"
        if player == "paper":
            if computer == "rock":
                return "You win"
            else:
                return "You lose"
        if player == "scissors":
            if computer == "paper":
                return "You win"
            else:
                return "You lose"
    
    def play_game(self):
        while True:
            player = self.player_choice()
            computer = self.computer_choice()

            result = self.determine_winner_or_tie(player, computer)
            print("You picked " + player)
            print("Computer picked " + computer)
            print(result)

            play_again = input("Would you like to play again? yes or no: ")
            if play_again.lower() != "yes":
                break



test = RockPaperScissors()
# print(test.player_choice())
# print(test.computer_choice())

test.play_game()