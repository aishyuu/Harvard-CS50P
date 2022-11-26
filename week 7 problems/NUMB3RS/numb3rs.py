"""
An IPv4 address is a numeric identifier used to communicate to internet
It's formatted in decimal notation where its
    #.#.#.#
    Each # should be a number >= 0 and <= 225
    
Implement a program that validates the input of an IPv4 adress
Output a string that returns True or False
"""

import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))
    
def validate(ip):
    test = re.search(r"([1-9]+)\.([1-9]+)\.([1-9]+)\.([1-9]+)", ip)
    if test:
        for group in test.groups():
            try:
                current_num = int(group)
            except ValueError:
                print("One of these are not a number")
                return(False)
                
            if current_num < 0 or current_num > 225:
                print("One of these numbers don't fit in the range of 225")
                return(False)
        
        return True
    
    else:
        return False
        
    
if __name__ == "__main__":
    main()