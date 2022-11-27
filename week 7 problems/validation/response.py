"""
Use a validator collection or validators from PyPI

Implement a program that asks the user for an email address via input
Print Valid or Invalid if the input is a valid email

You can't use re
Don't have to validate if the email domain exists
"""

from validator_collection import checkers

def main():
    is_email: checkers.is_email(input("Insert email address: "))
    if is_email:
        print("Valid")
    else:
        print("Invalid")
    
if __name__ == "__main__":
    main()