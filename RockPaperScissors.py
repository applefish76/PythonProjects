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
print("Lets play rock, paper,scissors!")
player_choice = int(input("Please type 0 for rock, 1 for paper and 2 for scissors\n"))
if player_choice == 0:
    print("You chose\n" + rock)
elif player_choice == 1:
    print("You chose\n" + paper)
elif player_choice == 2:
    print("You chose\n" + scissors)

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print ("computer chose\n" + rock)
elif computer_choice == 1:
    print ("computer chose\n" + paper)
elif computer_choice == 2:
    print ("computer chose\n" + scissors)

if player_choice == computer_choice:
        print("Draw")
elif computer_choice == 0 and player_choice == 2:
        print("Computer wins")
elif player_choice == 0 and computer_choice == 2:
        print("You win")
elif player_choice > computer_choice:
        print("You win")
elif computer_choice > player_choice:
        print("Computer wins")

