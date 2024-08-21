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

choose = int(input("Welcome to the game Rock Paper Scissors, what do you choose? Type 0 for rock, 1 for paper, and 2 for scissors "))
import random
game = [rock, paper, scissors]
random_index = random.randint(0,2)
computer = game[random_index]
print("Computer Choose:")
print(computer)
print("You Choose:")
print(game[choose])
if choose == random_index:
    print("It's a draw")
elif choose >= 3 or choose < 0:
    print("Invalid number")
elif choose == 0 and  random_index == 1:
    print("You are lose")
elif choose == 0 and random_index == 2:
    print("You are win")
elif choose == 1 and random_index == 0:
    print("You are win")
elif choose == 1 and random_index == 2:
    print("You are lose")
elif choose == 2 and random_index == 0:
    print("You are lose")
elif choose == 2 and random_index == 1:
    print("You are win")



