# Create a game called rock paper or scissors
# import libraries
import random


class Game:
    """Create a game for rock paper scissors"""

    def __init__(self):
        print("Welcome to the python Rock, Paper or Scissors championship \n")
        print("You shall compete against the machine")
        self.user_play()

    def user_play(self):
        self.choice = int(
            input(
                "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"
            )
        )
        self.comp_choice = random.randint(0, 2)
        winner = self.rule_check()
        self.commentate(winner)

    def rule_check(self):
        """
        Check who won between playerA and playerB
        Returns:
            int 0 - if computer wins and 1 if Human wins
        """
        if self.choice == self.comp_choice:
            print("Game is tied")
            self.play_again()
        elif (
            (self.choice == 0 and self.comp_choice == 1)
            or (self.choice == 1 and self.comp_choice == 2)
            or (self.choice == 2 and self.comp_choice == 0)
        ):
            print("Computer wins")
            return 1
        else:
            print("Congratulations, you won.")
            return 0

    def play_again(self):
        """
        Option to play Rock, Paper or Scissors again if game is tied.
        """
        choice = input("Type 'yes' to play again \n")
        if choice.lower() == "yes":
            self.user_play()
        else:
            return

    def commentate(self, winner: int):
        """
        Commentate what the user played and what the computer played
        Args:
            winner int: Who won the game, 0 - Human, 1 - computer
        """
        selection = list(map(self.map_choice, (self.choice, self.comp_choice)))
        print("Human Choice was {}".format(selection[0]))
        print("Computer Choice was {}".format(selection[1]))
        if isinstance(winner, int):
            print(
                "{} beats {}".format(selection[abs(winner)], selection[abs(winner - 1)])
            )

    def map_choice(self, player_choice):
        """
        Args:
            player_choice:
        Returns:
        """
        if player_choice == 0:
            return "Rock"
        elif player_choice == 1:
            return "Paper"
        elif player_choice == 2:
            return "Scissors"
        else:
            raise ValueError(
                "Your choice had to  0 for Rock, 1 for Paper or 2 for Scissors"
            )


if __name__ == "__main__":
    Game()
