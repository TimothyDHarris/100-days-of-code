# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is the name of the person you like? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
name1_lower_case = name1.lower()
name2_lower_case = name2.lower()

true = 0
true += name1_lower_case.count("t") 
true += name2_lower_case.count("t")
true += name1_lower_case.count("r") 
true += name2_lower_case.count("r")
true += name1_lower_case.count("u") 
true += name2_lower_case.count("u")
true += name1_lower_case.count("e") 
true += name2_lower_case.count("e")

love = 0
love += name1_lower_case.count("l") 
love += name2_lower_case.count("l")
love += name1_lower_case.count("o") 
love += name2_lower_case.count("o")
love += name1_lower_case.count("v") 
love += name2_lower_case.count("v")
love += name1_lower_case.count("e") 
love += name2_lower_case.count("e")

true_love = int(str(true) + str(love))

if true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
elif true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
else:
    print(f"Your score is {true_love}.")