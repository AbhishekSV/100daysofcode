#Day 12 App
import random
from os import system

def play_game():
    print("Welcome to the Number Guessing Game\n")
    print("I'm thinking a number between 1 to 100\n")
    number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        chances = 10
    elif difficulty == 'hard':
        chances = 5
    else:
        chances = 0
    while chances > 0:
        print(f"You've {chances} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print(f"You got it. The answer was {number}")
            return
        chances -= 1
    print(f"You've run out of guesses, you lose. The answer was {number}")

play_again = True
while play_again:
    play_game()
    choice = input("Do you want to play again? Enter 'y' or 'n': ")
    if choice == 'y':
        system('clear')
    else:
        print("Goodbye!")
        play_again = False
