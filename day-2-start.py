# Notes on Strings, Integers, Floats, and Booleans

# The number in the square brackets will determine what gets printed
# These are strings
print("Hello"[0])
print("Hello"[4])

# To declare an integer, just type out an integer (number)
# You can use underscores to better read large numbers and the computer will ignore them
# the plus sign works to add the intigers
addition = print(123 + 456)

# The Float type uses decimal points, like pi

# Boolean is only True or False
##################################################

# You can change data types. For example you can change an intiger into a string by using this function below
new_addition = str(addition)
print(type(new_addition))
# You can use the type function to tell you what kind of variable you are working with
print(type("Hello"))
# we can also convert something within the print
print(70 + float("100.5"))
# you can use str() int() or float() to convert your variables
##################################################

# how to do math in python
# addition
print("addition", 5 + 5)
# subtraction
print("subtraction", 7 - 4)
# multiplication
print("multiplication", 3 * 2)
# division
print("division", 6 / 3)
# raise to the power of
print("raise 2 to the power of (3)", 2 ** 3)
# round
print("round the value of this division", round(8 / 3))
# turn it into an integer without rounding when dividing
print("turn a division result into an integer", 8 // 3)
# you can also change a value by adding the math function to the beginning of the equals sign
score = 0
# this adds 1 to the value of score
score += 1
print("The score is", score)

##################################################
# f-String
print(f"you can mix and match variables by adding them within braces here with an 'f' at the beginning with no spaces")
