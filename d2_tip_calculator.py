#Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? "))
split = float(input("How many people to split the bill? "))

tip = tip / 100
total_bill = bill + (bill * tip)
split_bill = total_bill / split
print(f"Each person should pay: ${round(split_bill, 2)}")
