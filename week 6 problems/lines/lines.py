"""
Implement a program that expects exactly one command-line argument
The argument must be the name/path of a python file
Output the number of lines in that code

Errors should be met with sys.exit
    If it doesn't end with py
    If it doesn't exist
    If there are <2 or >2 arguments
    
When calculating the lines, exclude blank lines and comments ("#")
"""

import sys

def main():
    #Check if there are exactly 2 arguments
    try:
        if len(sys.argv) > 2:
            print("Too many arguments")
            raise ValueError
        if len(sys.argv) < 2:
            print("Too few arguments")
            raise ValueError
    except ValueError:
        sys.exit()

    #Check if the file even exists
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
    
    line_count = 0
    
    for line in file:
        if line.lstrip().startswith("#"):
            pass
        elif not line.strip():
            pass
        else:
            line_count += 1
            
    print(line_count)
        
if __name__ == "__main__":
    main()