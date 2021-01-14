# following along and coding as I watch the first videos

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# nested if else statement
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
        # elif statement, use if we have something between an if and else statement
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything will be okay, have a free ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you what a photo taken for an additional $3? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride!")