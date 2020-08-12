# NUMBER GAME JB
from random import randint

guess = int(input("Choose a number between 1 and 100")) # Ask the user
secret_number = randint(0, 100)   # generate secret number

a = 1  # a is use to count number of attempts

while guess != secret_number:
    if guess < secret_number:
        print("The secret number is bigger!")
        a = a + 1
        guess = int(input("Enter a number:"))
    else:
        print("The secret number is smaller!")
        a = a + 1
        guess = int(input("Enter a number:"))

if guess == secret_number:
    print("You won the game in " + str(a) + " attempts.")

print("Try to play again if you want")
