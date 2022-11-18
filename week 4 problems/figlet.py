"""
Implement a program that:
Expects 0 or two command line arguments

Zero if the user would like to output text in a random font

Two if the user would like to output text in a specific font
The first of the two should be "-f" or "--font"
Second should be the name of the font

Prompt the user for a str of text
Output text in desired font
"""

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def verify():
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            return
    sys.exit()
    

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    s = input("Input: ")
    print(f"Output: \n{figlet.renderText(s)}")
    sys.exit()

if len(sys.argv) == 3:
    verify()
    figlet.setFont(font=sys.argv[2])
    s = input("Input: ")
    print(f"Output: \n{figlet.renderText(s)}")