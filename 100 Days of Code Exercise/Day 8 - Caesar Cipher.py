# Implement Caeser Cipher Code
class CaeserCipher:
    """Implement Caeser Cipher. In Caeser Cipher each letter is shifted by 4."""

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
        ]
        self.shift = int(input("Shift letter by (Enter an integer): \n"))
        self.method = input(
            "Do you want to encode or decode? (Type 'encode' or 'decode'): \n"
        ).lower()
        self.message = input("Enter your message: \n").lower()
        self.performOperation()

    def performOperation(self):
        crypt_msg = []
        if self.method == "encode":
            shift = self.shift
        elif self.method == "decode":
            shift = -self.shift
        else:
            raise ValueError("Expected method 'encode' or 'decode'")
        for i in self.message:
            if i in self.letters:
                updated_index = (self.letters.index(i) + shift) % 25
                crypt_msg.append(self.letters[updated_index])
            else:
                crypt_msg.append(i)
        crypt_msg = "".join(crypt_msg)
        print("Here is your {} d message {}.".format(self.method, crypt_msg))


if __name__ == "__main__":
    CaeserCipher()
