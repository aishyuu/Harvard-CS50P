"""
When texting, we tend to shorten words
Implement a program that prompts for a string
Output the text but with all vowels(A,E,I,O,U) omitted
"""

def main():
    to_check = input("Input: ")
    print(remove_vowel(to_check))

def remove_vowel(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() not in ("a", "e", "i", "o", "u"):
            result += letter

    return result

main()