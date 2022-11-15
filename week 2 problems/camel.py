"""
Python, compared to other languages, recommends snake case
Snake case is where variables with multiple words are seperated by "_"
Implement a program that prompts the user for the name of a variable in Camel
Output the corresponding name in snake case
Assume that the user's input will be in camel case
"""

def main():
    variable = input("camelCase: ")
    print(snake_case(variable))

def snake_case(camel):
    result = ""
    for letter in camel:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter
    return result

main()