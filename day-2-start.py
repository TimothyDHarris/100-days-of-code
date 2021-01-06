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
# ----------------------------------------------------------------------------------------------------------

# You can change data types. For example you can change an intiger into a string by using this function below
new_addition = str(addition)
print(type(new_addition))
# You can use the type function to tell you what kind of variable you are working with
print(type("Hello"))
# we can also convert something within the print
print(70 + float("100.5"))
# you can use str() int() or float() to convert your variables