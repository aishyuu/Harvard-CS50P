"""
Implement a program that
Prompts the user for a level
    If they don't input 1, 2, or 3, the program prompts again
    The levels mean the number of digits
    So...
        Level 1 = 1-9
        Level 2 = 1-99
        level 3 = 1-999
    
Randomly generate 10 math problems formatted as
    X + Y =
Where X and Y are non-negative integers

If they get it right, they get a point
If they get it wrong, remove a point 

By the end tell the user their score out of 10
"""
import random

def game(level):
    score = 10
    for _ in range(1, 11):
        #Get a random int from 1 to 10^level - 1 (Will result in desired digits)
        x = random.randint(1, 10 ** level -1)
        y = random.randint(1, 10 ** level -1)
        #Set the correct answer and a variable to True
        correct_answer = x + y
        correct = True
        
        while True:
            try:
                #Keep asking the user for the correct answer
                user_answer = int(input(f"{x} + {y} = "))
                #If false, the switch fill turn false, print error, and restart
                if user_answer != correct_answer:
                    correct = False
                    print("EEE")
                    raise ValueError
                break
            except ValueError:
                pass
        #Check at the end if the score is false, if yes, take 1 from score
        if correct == False:
            score -= 1
    #Return score at the end
    return score
    

def main():
    #Ask the user for the level
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            else:
                break 
        except ValueError:
            pass

    print(game(level))
    
main()