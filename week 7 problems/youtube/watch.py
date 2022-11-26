"""
Suppose you want to extract the URL of youtube videos embedded in HTML
    https://www.youtube.com/embed/xvFZjo5PgG0
    and convert them to shorter, sharable URLs
    https://youtu.be/xvFZjo5PgG0
    
Implement a program that accepts HTML as input

You extract the youtube URL from the HTML
Convert it to a shorter sharable link

Assume...
    Value of src will be in double quotes
    The input will contain no more than one such URL
    
If the input does not contain any URL, return None

Ways the URL can be formatted
    http://youtube.com/embed/xvFZjo5PgG0
    https://youtube.com/embed/xvFZjo5PgG0
    https://www.youtube.com/embed/xvFZjo5PgG0
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Search through the link using regular expression
    link = re.search(r"https?://(www\.)?youtube.com/embed/(\w+)", s)
    if link:
        # If link is found, return shortened link
        return f"https://youtu.be/{link.group(2)}"
    else:
        # Else, return None
        return None


if __name__ == "__main__":
    main()
