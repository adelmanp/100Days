#!/usr/bin/python3

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

#Write your code below this line 👇
import random
from sys import exit


options = ["rock", "paper", "scissors"]
choice = input("Would you like to play Rock, Paper, or scissors? \n").lower()
computer = random.choice(options).lower()


def ascii_art(move):
    if move == "rock":
        print(rock)
    elif move == "paper":
        print(paper)
    elif move == "scissors":
        print(scissors)
    else:
        print(f"{move} is not a valid move")
        print("You have been disqualified")
        exit()

print(f"You play {choice}")
ascii_art(choice)
print(f"The computer plays {computer}")
ascii_art(computer)

if choice == "rock" and computer == "paper":
  print("Paper beats Rock, \nYou Lose")
elif choice == "rock" and computer == "scissors":
  print("Rock beats Scissors, \nYou Win!")
elif choice == "rock" and computer == "rock":
  print("Alright, we'll call it a draw")

elif choice == "paper" and computer == "scissors":
  print("Scissors beats paper \nYou Lose")
elif choice == "paper" and computer == "rock":
  print("Paper beats Rock, \nYou Win!")
elif choice == "paper" and computer == "paper":
  print("Alright, we'll call it a draw")

elif choice == "scissors" and computer == "rock":
  print("Rock beats Scissors, \nYou Lose")
elif choice == "scissors" and computer == "paper":
  print("Scissors beats Paper, \nYou Win!")
elif choice == "scissors" and computer == "scissors":
  print("Alright, we'll call it a draw")
