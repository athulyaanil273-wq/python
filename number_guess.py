import random

number = random.randint(1, 10)

print("Guess the Number!")
print("I have chosen a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Correct! You guessed it!")
else:
    print("Wrong guess!")
    print("The correct number was:", number)
