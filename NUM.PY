# Import necessary modules
import random
import time

from matplotlib.pylab import block

# Pick a number between 1 and 100
number=random. randint(1, 100)

def intro():
    print("May I ask you for your name?")
    # declaring name variable global so it can be accessed outside the function
    global name
    name = input() #asks for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    if(number%2 == 0):
        x='even'
    else:
        x='odd'
    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():
    guessesTaken = 0

    #if the number of guesses is less than 6
    while guessesTaken < 6:
        time.sleep(.25)
        #inserts the place to enter guess
        enter=input("Guess: ")
        #check if a number was entered
        try:
            #stores the guess as an integer instead of a string
            guess = int(enter)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess <= 100 and guess>=1: #if they are in range
            guessesTaken=guessesTaken+1 #adds one guess each time
            if guessesTaken<6:
                if guess<number:
                    print("The guess of the number that you have entered is too low")
                if guess>number:
                    print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")

                    #if the guess is right, then we are going to jump out of the while block

                    if guess == number:
                        break

                    if guess>100 or guess<1:
                        print("Silly Goose! That number isn't in the range!")
                        time.sleep(.25)
                        print("Please enter a number between 1 and 100")

                    if guess == number:
                        guessesTaken = str(guessesTaken)
                        print('Good job, {}! You guessed my number in {} guesses!'.format(name, guessesTaken))
