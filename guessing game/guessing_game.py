#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 18:38:02 2019

@author: sandeep
"""

from random import randint

random = randint(1,100)  # assings a random integer to the random variable

# below are the rules


print("Welcome to Guessing game!!!!!")
print("Rules for playing the game are following:")
print("1. Guess a number between 1 and 100")
print("2. If your guessed number is 10 numbers far from my number then I will tell you're 'COLD!'")
print("3. If your guessed number is within 10 number of my number I'll tell you're 'WARM!'" )
print("4. If your guess is farther from your previous guess then I will tell you're getting 'COLDER!' ")
print("5. If your guess is closer to your previous guess then I'll tell you're getting 'WARMER!'")
print("Now let's start the game")

# creating a list to store the guesses giben by the user

guesses = [0]

# this loop gets the input and evaluates

while True:

    
        guess = int(input("Guess a number between 1 and 100\n")) # input guess
    
        if guess < 1 or guess >100:   # range
            print("OUT OF BOUNDS!")
            continue
    
    
    
        if guess == random:
            print(f"You have guessed correctly and took {len(guesses)} guesses")
            break
            
        guesses.append(guess)  # appending current guess to list of guesses
            
        if guesses[-2]:  # guesses[-2] is the previous guess
        
            if abs(guess - random)< abs(random - guesses[-2]):  # abs gives the absolute difference between two integers
                # if current guess is less than previous guess i.e. guess is closer
                print("WARMER!")
            else:
                print("COLDER!")
            
        else:
            if abs(guess - random) <= 10:   # if the guess is closer within 10 numbers
                print("WARM!")
            else:
                print("COLD!")
