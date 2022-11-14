"""
Implement a program that prompts the user for an arithmetic expression
Calculate this expression
Output the result as a foating-point value formatted to one decimal place
Assume the user's input will be formatted as
    x y z
    With one space between x and y and one space between y and z

    x is an integer
    y is +, -, *, or /
    z is an integer

For example:
    1 + 1
    Should output 2.0
"""

def main():
    expression = input("Expression: ")
    print(interpret(expression))

def interpret(exp):
    x, y, z = exp.split(" ")
    match y:
        case "+":
            return(round(float(x) + float(z), 1))
        case "-":
            return(round(float(x) - float(z), 1))
        case "*":
            return(round(float(x) * float(z), 1))
        case "/":
            return(round(float(x) / float(z), 1))

main()