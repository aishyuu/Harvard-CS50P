"""
An IPv4 address is a numeric identifier used to communicate to internet
It's formatted in decimal notation where its
    #.#.#.#
    Each # should be a number >= 0 and <= 225
    
Implement a program that validates the input of an IPv4 adress
Output a string that returns True or False
"""

import re

def main():
    print(validate(input("IPv4 Address: ")))
    
def validate(ip):
    #Check if the input is correct through regular expressions
    test = re.search(r"([1-9]+)\.([1-9]+)\.([1-9]+)\.([1-9]+)", ip)
    #If the input passes the regular expressions check
    if test:
        #For every group (...) in the regular expression
        for group in test.groups():
            try:
                #Try to convert the current group into an integer
                current_num = int(group)
            except ValueError:
                #If it doesn't work, return False
                print("One of these are not a number")
                return(False)
            #If the current group is an integer, check if it's between 0 and 225
            if current_num < 0 or current_num > 225:
                print("One of these numbers don't fit in the range of 225")
                return(False)
        
        return True
    
    else:
        return False
        
    
if __name__ == "__main__":
    main()