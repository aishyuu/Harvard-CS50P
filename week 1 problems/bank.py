"""
1. Prompt the user for a greeting
    If the greeting starts with "hello" -> output $0
    If the greeding starts with an "h" -> output $20
    Else -> output $100
2. Ignore any leading whitespace in the user's greeting
*Treat user's greeting case-insensitively*
"""

def main():
    greeting = input("Greeting: ")
    print(greet_check(greeting))

def greet_check(greeting):
    stripped_greet = greeting.split()[0].lower()
    if stripped_greet[0:5] == "hello":
        return "$0"
    elif stripped_greet[0] == "h":
        return "$20"
    else:
        return "$100"

main()