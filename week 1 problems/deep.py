"""
Implement a program that prompts the user for the answer for...
Life, the Universe, and Everything
Outputting Yes IF the user inputs 42, forty-two, or forty two
Else type no
"""

def main():
    user_Input = input("What is the answer to Life, the Universe, and Everything? ")
    print(verify_answer(user_Input))
    

def verify_answer(answer):
    answer = answer.strip().lower()
    match answer:
        #Check if it's one of the 3 we want
        case "42" | "forty-two" | "forty two":
            return "Yes"
        #If it's anything else we return false
        case _:
            return "No"

main()