# Mekedelawit E. Hailu 

# "Guess the number" 
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

# initialize global variables used in your code

secret_number = random.randrange(0, 100)
guesses = 7
num_range = 100


# helper function to start and restart the game

def new_game():
    global num_range
    if(num_range == 100):
        range100()
    else:
        range1000()


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
       
    print "New game. Range is from 0 to 100"
    
    global guesses, num_range
    guesses = 7
    num_range = 100
    
    print "Number of remaining guesses is", guesses, "\n"
    
    global secret_number
    secret_number = random.randrange(0, 100)
    return secret_number

def range1000():
    # button that changes range to range [0,1000) and restarts
        
    print "New game. Range is from 0 to 1000"
    
    global guesses, num_range
    guesses = 10
    num_range = 1000
    
    print "Number of remaining guesses is", guesses, "\n"
    
    global secret_number
    secret_number = random.randrange(0, 1000)
    return secret_number
    
def input_guess(guess):
    # main game logic goes here
    
    print "Guess was", guess
    
    global secret_number, guesses
    guesses = guesses - 1
    guess = int(guess)
    print "Number of remaining guesses is", guesses
    if secret_number > guess:
        if guesses == 0:
            print "You ran out of guesses. The number was", secret_number, "\n"
            new_game()
        else:
            print "Higher!\n"         
    elif secret_number < guess:
        if guesses == 0:
            print "You ran out of guesses. The number was", secret_number, "\n"
            new_game()
        else:
            print "Lower!\n"
    else :
        print "Correct!\n"
        new_game()
    
        
# create frame

frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements

frame.add_button("Range is [0 to 100)", range100, 200)
frame.add_button("Range is [0 to 1000)",range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game()
frame.start()

