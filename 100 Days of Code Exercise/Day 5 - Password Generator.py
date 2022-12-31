# Create a Password Generator

import random


class PasswordGenerator:
    """Password Generator"""

    def __init__(self):
        self.letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
        self.createPassword()

    def createPassword(self):
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        self.characters = [random.choice(self.letters) for _ in range(nr_letters)]
        self.characters.extend([random.choice(self.symbols) for _ in range(nr_symbols)])
        self.characters.extend([random.choice(self.numbers) for _ in range(nr_numbers)])
        random.shuffle(self.characters)
        print(''.join(self.characters))


if __name__ == "__main__":
    PasswordGenerator()
