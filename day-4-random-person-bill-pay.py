# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# #Write your code below this line 👇
# Note, I am not allowed to use the choice(function)
import random
random.shuffle(names)
print(f"{names[0]} is going to buy the meal today")