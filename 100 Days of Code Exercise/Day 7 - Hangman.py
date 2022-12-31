# Play Hangman


class Hangman:
    """Implement the game hangman"""

    def __init__(self, word, life=7):
        """
        Args:
            word str: word to guess
            life int: number of guesses allowed
        """
        self.word = word.lower()
        self.life = life
        self.word_list = [s for s in self.word]
        self.len_word = len(self.word)
        self.hangman_word = ["_"] * self.len_word
        self.guessed_letter = set()
        self.guess()

    def guess_word(self, letter):
        """
        Args:
            letter str: Letter to be guess
        """
        if letter in self.word:
            for i, char in enumerate(self.word_list):
                if char == letter:
                    self.hangman_word[i] = char
        else:
            self.life -= 1
            print()
        self.guessed_letter.add(letter)

    def guess(self):
        while self.life != 0:
            wrd = input("Enter a letter \n").lower()
            if len(wrd) != 1:
                raise ValueError("Expected one letter")
            if wrd in self.guessed_letter:
                print("You have already guessed this letter.")
            self.guess_word(wrd)
            print(" ".join(self.hangman_word))
            if self.hangman_word == self.word_list:
                print("You guess the correct word which is " + self.word)
                break
            print("You have {} life left".format(self.life))
            print("Guessed letters {}".format(self.guessed_letter))


if __name__ == "__main__":
    Hangman("batman")
