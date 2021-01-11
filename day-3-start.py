# following along and coding as I watch the first videos

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# nested if else statement
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
        # elif statement, use if we have something between an if and else statement
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride!")