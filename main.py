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
import random
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if your_choice == 0:
  print("You chosed: rock"+rock)
elif your_choice == 1:
  print("You chosed: paper"+paper)
elif your_choice == 2:
  print("You chosed: scissors"+scissors)
else:
  print("Not a valid input.")
  
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print("Computer chosed: rock"+rock)
elif computer_choice == 1:
  print("Computer chosed: paper"+paper)
elif computer_choice == 2:
  print("Computer chosed: scissors"+scissors)

if your_choice == 0 and computer_choice == 1:
  print("You Lose.")
elif your_choice == 0 and computer_choice == 2:
  print("You Win!")
elif your_choice == 1 and computer_choice == 0:
  print("You Win!")
elif your_choice == 1 and computer_choice == 2:
  print("You Lose.")
elif your_choice == 2 and computer_choice == 0:
  print("You Lose.")
elif your_choice == 2 and computer_choice == 1:
  print("You Win!")
else:
  print("Tie.")