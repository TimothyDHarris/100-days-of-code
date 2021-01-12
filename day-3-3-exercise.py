# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# Below is my first attempt at coding for testing for a new year. However, my logic was not interconnected enough and the check was not roboust enough.
# if (year % 4 == 0):
#     print(f"The year {year} is a leap year.")
# elif (year % 100 != 0 and year % 400 == 0):
#     print(f"The year {year} is a leap year.")
# else:
#     print(f"The year {year} is not a leap year.")

# Teacher's solution below with some edits from me
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else: 
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")