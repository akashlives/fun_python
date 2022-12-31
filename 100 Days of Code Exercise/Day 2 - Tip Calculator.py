# Create a Tip Calculator
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
n_people = int(input("How many people to split the bill?"))
pay_per = (bill * (1 + (tip_percent / 100))) / n_people
print("Each person should pay: ${}".format(round(pay_per, 2)))
