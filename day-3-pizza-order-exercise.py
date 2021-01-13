# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want to add pepperoni for $2? Y or N: ")
extra_cheese = input("Do you want to add extra cheese for $1? Y or N: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
if size == "M":
    bill += 20
if size == "L":
    bill += 25
if add_pepperoni == "Y":
    bill += 2
if extra_cheese == "Y":
    bill += 1
print(f"Your total comes to: ${bill}.")