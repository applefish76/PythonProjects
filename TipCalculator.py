print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n£"))
tip_percentage = int(input("What percentage tip would you like to give? \n10% 12% 15% \n"))
people = int(input("How many people to split the bill? \n"))

# tip = (bill*(tip_percentage/100))
tip = bill * (tip_percentage / 100)

print(f"Each person should pay: £{round((bill + tip)/people, 2)}")
