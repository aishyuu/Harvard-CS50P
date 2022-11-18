"""
Prompt the user for a level
If the user doesn't input a positive integer, it asks again
Generate a number between 1 and the number chosen

Then, prompt the user to guess that integer
If the guess is smaller, output "Too Small" then prompt the user again
If the guess is bigger, output "Too Big" then prompt the user again
"""

import random

while True:
    try:
        level = int(input("Level: "))
        if(level < 1): 1/0
        break
        
    except (ValueError, ZeroDivisionError):
        pass

answer = random.randint(1, level)
    
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    
    if guess > answer:
        print("Too big!!")
    elif guess < answer:
        print("Too Small!")
    else:
        print("Just right!")
        break
        