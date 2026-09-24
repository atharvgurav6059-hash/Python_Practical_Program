'''Write a Python program to implement a number guessing game in which the user
 repeatedly enters guesses until the correct number is found.
   Display whether each guess is too high or too low.'''

secret = 50

guess = int(input("Guess the number: "))

while guess != secret:

    if guess > secret:
        print("Too high")

    else:
        print("Too low")

    guess = int(input("Guess again: "))

print("Correct! You guessed the number.")