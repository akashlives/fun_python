# Create a simple Calculator


class Calculator:
    """Simple Calculator that can add, subtract, multiply or divide"""

    def __init__(self):
        self.n1 = float(input("Enter your first number (expecting int or float): \n"))
        operation = input("Type '+' , '-', '*' or '/' \n")
        self.n2 = float(input("Enter your second number (expecting int or float): \n"))
        self.ops_dict = {
            "+": self.add(),
            "-": self.subtract(),
            "*": self.multiply(),
            "/": self.divide(),
        }
        print(
            "{} {} {} = {}".format(
                self.n1, operation, self.n2, self.ops_dict[operation]
            )
        )

    def add(self):
        """
        Add 2 numbers
        Returns:
            sum int or float: Summation of two numbers n1 and n2
        """
        return self.n1 + self.n2

    def subtract(self):
        """
        Subtract 2 numbers
        Returns:
            diff int or float: Difference of two numbers n1 and n2
        """
        return self.n1 - self.n2

    def multiply(self):
        """
        Multiply 2 numbers
        Returns:
            mul int or float: Multiplication of two numbers n1 and n2
        """
        return self.n1 * self.n2

    def divide(self):
        """
        Divide 2 numbers
        Returns:
            div int or float: Division of two numbers n1 and n2
        """
        return self.n1 / self.n2


if __name__ == "__main__":
    Calculator()
