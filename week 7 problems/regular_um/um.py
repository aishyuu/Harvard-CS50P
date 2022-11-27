"""
Implement a function called count
expects a line of text as a str and returns an int
This int is the number of times 'um' appears in text
    Case insensitively

Given text 'hello, um, world' --> 1
Yummy would output 0
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"[Uu][mM][\s,\.]", s, re.IGNORECASE)
    return len(um)


if __name__ == "__main__":
    main()
