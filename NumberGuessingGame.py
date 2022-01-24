#import random and time module
import random
import time

#create a random number from range between 1-100
n = random.randrange(1,100)

#write a welcome message
print("Welcome to the NUMBER GUESSING GAME!\nYou have only 8 attempts to Guess.")

#give 2 sec. delay
time.sleep(2)

# take a user input to enter a number
guess=int(input("Guess a number: "))

count = 1

#use loops to create conditions

while n != guess and count<8:
    #if guess is smaller than n
    if guess < n:
        print("Go Higher")
        print("You have {} attempts left.".format((8-count)))
        guess=int(input("Guess again: "))
        count+=1
    #if guess is greater than n
    elif guess>n:
        print("Go Lower")
        print("You have {} attempts left.".format((8-count)))
        guess=int(input("Guess again: "))
        count+=1
    else:
        break

if n==guess:
    print("*** You guessed correctly. Good job! ***")
else:
    print("Unlucky, Try Again!")
