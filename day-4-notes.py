# Section 1
# below is how we can import something into our code.
# We can do this with things from the python team or our other files.
import random

# randint(a, b) allows us to get a psuedorandom number that is in integer
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

# Section 2
some_states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
# number on the end picks, in brackets, the 3rd item from the list
print(some_states_of_america[3])
# Using .append will add an item to the end of the list
some_states_of_america.append("Massachusetts")
print(some_states_of_america)

# Python docs for data structures https://docs.python.org/3/tutorial/datastructures.html

# Using .extend adds another list to the end of the first list
some_states_of_america.extend(["Maryland", "South Carolina", "New Hampshire"])
print(some_states_of_america)
# You can also use a negative number to pull from the back of the list
print(some_states_of_america[-1])

# You can nest lists inside a list
food = ["hotdog", "burger", "fries"]
condiments = ["catchup", "mustard", "relish"]
menuList = [food, condiments]
print(menuList)