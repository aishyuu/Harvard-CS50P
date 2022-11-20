"""
Implement a program that prompts the user for a fraction
X / Y, where X and Y are integers
Outputs how much fuel is in the tank
If it's <= 1%, output E
If it's >= 99%, output F

if X or Y are not integers, X > Y, or Y == 0, prompt the user again
"""

def main():
    while True:
        try:
            fraction = input("Fraction ")
            x, y = fraction.split("/")
            x,y = int(x), int(y)
            if x > y:
                death = 1/0
        except (ValueError, ZeroDivisionError):
            pass

    print(get_expression(x,y))
    

def get_expression(x, y):
    #I mean...99.9 to int is 99 but it still fits condition lol
    result = int((x/y) * 100)
    if result <= 1:
        return "E"
    elif result >= 99:
        return "F"
    else:
        return f"{result}%"
            
if __name__ == "__main__":    
    main()