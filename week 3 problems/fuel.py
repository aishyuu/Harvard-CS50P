"""
Implement a program that prompts the user for a fraction
X / Y, where X and Y are integers
Outputs how much fuel is in the tank
If it's <= 1%, output E
If it's >= 99%, output F

if X or Y are not integers, X > Y, or Y == 0, prompt the user again
"""

def main():
    print(get_expression())
    

def get_expression():
    while True:
        try:
            #Prompt user for fraction
            fraction = input("Fraction: ")
            #Assign x and y to their respective letter
            x,y = fraction.split("/")
            #Make x and y integers (they're still string until this point)
            x,y = int(x), int(y)
            if x > y:
                #Causes error if x > y, causing a restart
                death = 1/0
            else:
                #I mean...99.9 to int is 99 but it still fits condition lol
                result = int((x/y) * 100)
                if result <= 1:
                    return "E"
                elif result >= 99:
                    return "F"
                else:
                    return f"{result}%"
        #This is to catch values that aren't int and when you divide 0
        except (ValueError, ZeroDivisionError):
            pass
            
            
main()