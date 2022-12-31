# Find the treasure in treasure island
class Game:
    """Treasure island game"""

    def __init__(self):
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.")
        self.road_choice()

    def road_choice(self):
        road = input(
            "You're at a cross road. Where do you wan to go? Type 'left' or 'right' \n"
        )
        if road.lower() == "right":
            print("Game Over")
        elif road.lower() == "left":
            self.swim_choice()
        else:
            raise ValueError("Expected value was either 'left' or 'right'")
        return

    def swim_choice(self):
        swim = input(
            "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to "
            "swim across. \n "
        )

        if swim.lower() == "swim":
            print("Game Over")
        elif swim.lower() == "wait":
            self.door_choice()
        else:
            raise ValueError("Expected value was either 'swim' or 'wait'")
        return

    def door_choice(self):
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which "
            "color do you choose? \n"
        )
        if door.lower() == "red" or door.lower() == "blue":
            print("Game Over")
        elif door.lower() == "yellow":
            print("You win")
        else:
            raise ValueError("Expected value to be either 'blue', 'red' or 'yellow'")


if __name__ == "__main__":
    Game()
