# Instead of 'Treasure Island' I decided to do 'Rocky Mountain Hike Adventure'

print("Welcome to a Rocky Mountain Hike Adventure")
print('''
("`-''-/").___..--''"`-._ 
 `6_ 6  )   `-.  (     ).`-.__.`) 
 (_Y_.)'  ._   )  `._ `. ``-..-' 
   _..`--'_..-_/  /--'_.'
  ((((.-''  ((((.'  (((.-' 
  ''')
print("Your mission is to escape the mountain lion")
# decision flow chart below
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
direction = input('You are about to start hiking on a trail. You see two trailheads. Do you take the left one or the rignt one?\nType "left" for the left path and "right" for the right path.\n').lower()
if direction == "left":
    path = input('This trail seems pretty safe. You see a boulder up ahead. Do you stay on the path or try climbing up the boulder?\nType "boulder" to try and climb the boulder or type "path" to stay on the path \n').lower()
    if path == "path":
        alone = input('Now you come across two other hikers.\nDo you go with the hiker going the same direction as you, the opposite direction as you, or do you stay hiking by yourself?\nType "same" to hike with the hiker going the same direction.\nType "opposite" to go the opposite direction from where you are going.\nOr type "alone" to keep hiking on your own\n').lower()
        if alone == "opposite":
            print("You made a new friend and had a safe hike. Hiking with other people is a good way to scare off mountain lions. You made the right choice and you win!")
        elif alone == "same":
            print("You set off with the other hiker. However, you part ways very quickly when you want to hike to the lake but the other hiker does not.\nWhen you are alone again, the mountain lion strikes! ... you died.")
        else:
                print("You started singing a song as you hiked all alone. The mountain lion heard how off tune you were and it drove him crazy. He killed you to make you shut up.")
    else:
        print("When you started climbing up the boulder, a mountain lion saw you and attacked you... you died.")
else:
    print("The mountain lion was waiting on the right path for a foolish traveler... you died.")