"""
All vanity plates must start with 2 letters
Vanity plates may contain a maximum of 6 char
Vanity plates may contain a minimum of 2 char
Numbers can't be used in the middle of the plate
    AAA222 is good
    AAA22A is not good

First number used cannot be 0
No Periods, Spaces, or Punctuation marks are allowed
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#This function goes through a bunch of checks to make sure it's valid
def is_valid(s):
    #Length Requirement
    if len(s) < 2 or len(s) > 6:
        return False
    #Check if first 2 are letters
    if s[0:2].isalpha() == False:
        return False
    #Check if the length is greater than 2 to check
    if len(s) > 2:
        #Go through the user input from index 2 to the end
        for i in range(2, len(s)):
            #If the current index equals 0 and the previous is a letter
            if s[i] == "0" and s[i-1].isalpha():
                return False
            #If the current index is a "."
            if s[i] == ".":
                return False
            #If the current index is a letter and the one before is a number
            #Lines up with AAA22A is not good
            if s[i].isalpha() and s[i-1].isnumeric():
                return False

    #Return true because then it would have completed all conditions
    return True


main()