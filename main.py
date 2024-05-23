import art
import random

attempts = 1
game_active = True
number = random.randint(1, 100)

def low_high(guess, number):
  if guess > number:
    print("Too high.")
  elif guess < number:
    print("Too low.")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5
else:
  print("You did not select a correct difficulty.")

print(f"You have {attempts} attempts remaining to guess the number!")

while game_active:
  guess = int(input("Make a guess: "))
  attempts -= 1
  if guess == number:
    print(f"You have guessed the number {number}, you win!")
    game_active = False
  else:
    if attempts > 0:
      low_high(guess, number)
      print(f"You have {attempts} attempts remaining to guess the number, try again.")
    else:
      print(f"You have {attempts} attempts remaining, you lose! The number was {number}.")
      game_active = False