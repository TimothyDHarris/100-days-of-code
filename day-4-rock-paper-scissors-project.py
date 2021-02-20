import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rockPaperScissorsList = [rock, paper, scissors]
NPC_Choice = random.randint(0, 2)
Person_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print(rockPaperScissorsList[Person_Choice])
if Person_Choice == NPC_Choice:
    print(f"Computer chose:\n{rockPaperScissorsList[NPC_Choice]}")
    print("You tie")
elif Person_Choice == 0 and NPC_Choice == 1:
    print(f"Computer chose:\n{rockPaperScissorsList[NPC_Choice]}")
    print("You lose")
elif Person_Choice == 0 and NPC_Choice == 2:
    print(f"Computer chose:\n{rockPaperScissorsList[NPC_Choice]}")
    print("You win")
elif Person_Choice == 1 and NPC_Choice == 0:
    print(f"Computer chose:\n{rockPaperScissorsList[NPC_Choice]}")
    print("You win")
elif Person_Choice == 1 and NPC_Choice == 2:
    print(f"Computer chose:\n{rockPaperScissorsList[NPC_Choice]}")
    print("You lose")
elif Person_Choice == 2 and NPC_Choice == 0:
    print(f"Computer chose:\n{rockPaperScissorsList[NPC_Choice]}")
    print("You lose")
elif Person_Choice == 2 and NPC_Choice == 1:
    print(f"Computer chose:\n{rockPaperScissorsList[NPC_Choice]}")
    print("You win")
