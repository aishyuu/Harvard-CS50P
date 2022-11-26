'''
The US tends to use a 12-hour clock.
Instead of 09:00 to 17:00, we use 9:00 AM to 5:00 PM
    AM and PM will be capitalized (no periods therein)
    There will be a space before each
    
Make a program that translates the 12 hour format to the 24 hour format
    9:00 AM to 5:00 PM
    9 AM to 5 PM
    Both are valid inputs
    
Raise a ValueError if the input is not in either of these formats
or
Raise a ValueError if the time is invalid (12:60 AM, 13:00 PM)
'''

import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    before_time = re.search(r"(\d*:\d* [AP]M) to (\d*:\d* [AP]M)", s)
    after_times = []
    if before_time:
        for group in before_time.groups():
            hr, min = group.split(":")
            min, half = min.split(" ")
            after_times.append(validate(hr, min, half))
    else:
        return "Not Valid"
    
    return(f"{after_times[0]} to {after_times[1]}")
    
def validate(hr, min, half):
    hr = int(hr)
    min = int(min)
    if hr > 12 or hr < 0:
        print("Hour for one or more times are invalid")
        sys.exit()
    if min > 59 or min < 0:
        print("Minute for one or more are invalid")
    if half == "PM":
        if hr != 12:
            hr += 12
    if half == "AM" and hr == 12:
        hr = 0
    
    return(f"{hr}:{min}")
    
if __name__ == "__main__":
    main()