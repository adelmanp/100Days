#!/usr/bin/python3

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo_title


def intro():
    print(logo_title)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if difficulty == 'easy':
        guesses = 10
        print(f"You have {guesses} attempts remaining to guess the number")
    else:
        guesses = 5
        print(f"You have {guesses} attempts remaining to guess the number")
    return guesses


def play(answer, num_guesses):
    play = True
    while play:
        num_guesses -= 1
        guess = int(input("Make a guess: "))
        if num_guesses == 0:
            print("You've run out of guesses, you lose :-(")
            play = False
        elif guess == answer:
            print(f"You got it! The answer was {answer}")
            play = False
        elif guess > answer:
            print("Too high.")
            print("Guess again.")
            print(
                f"You have {num_guesses} attempts remaining to guess the number"
            )
        elif guess < answer:
            print("Too low.")
            print("Guess again.")
            print(
                f"You have {num_guesses} attempts remaining to guess the number"
            )


intro()
attempts = choose_difficulty()
random_num = random.randint(1, 100)
# print(f"[DEBUG] The correct answer is {random_num}")
play(random_num, attempts)
