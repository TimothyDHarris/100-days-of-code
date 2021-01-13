#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to your bill splitter calculator!")
bill_total = input("What is the bill total? $")
tip = input("What percentage tip would you all like to give? i.e. 10, 15, or 20? ")
how_many_ways = input("How many people are splitting this bill? ")
tip_float = float(tip) / 100 + 1.00

calculation = (float(bill_total) / float(how_many_ways)) * tip_float
calculation_two_decimals = "{:.2f}".format(calculation)

print(f"Each person sould pay: $ {calculation_two_decimals}")
