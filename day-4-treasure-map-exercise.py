# web address for exercise: https://repl.it/@appbrewery/day-4-3-exercise

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
firstPosition = int(position[0]) - 1
secondPosition = int(position[1]) - 1
if firstPosition == 0:
    if secondPosition == 0:
        row1.insert(0, "X")
    elif secondPosition == 1:
        row1.insert(1, "X")
    elif secondPosition == 2:
        row1.insert(2, "X")
elif firstPosition == 1:
    if secondPosition == 0:
        row2.insert(0, "X")
    elif secondPosition == 1:
        row2.insert(1, "X")
    elif secondPosition == 2:
        row2.insert(2, "X")
elif firstPosition == 2:
    if secondPosition == 0:
        row3.insert(0, "X")
    elif secondPosition == 1:
        row3.insert(1, "X")
    elif secondPosition == 2:
        row3.insert(2, "X")

row1 = row1[:3]
row2 = row2[:3]
row3 = row3[:3]
#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")