"""
Implement a program that prompts the user for their date of birth
    YYYY-MM-DD

Format and print how old they are in minutes.
    Round to the nearest integer
    
Assume for simplicity, the user was born at midnight
ALSO ASSUME THE TIME OF THE CURRENT DAY IS ALSO MIDNIGHT

Use datetime.date.today to get today's date
"""

from datetime import date
import sys
import re
import inflect

def main():
    #Ask user for date of birth
    birth_date = get_day(input("Date of Birth: "))
    current_date = date.today()
    result = int(str(current_date - birth_date).split(" ")[0])
    print(f"{inflect.engine().number_to_words(result*1440)} minutes")
    

def get_day(s):
    #Use regular expression to 
    birth_date = re.search(r"(\d\d\d\d)-(\d\d)-(\d\d)", s)
    if birth_date:
        birth_year, birth_month, birth_day = birth_date.groups()
        return(date(int(birth_year), int(birth_month), int(birth_day)))
    else:
        print("Not Valid")
        sys.exit()

if __name__ == "__main__":
    main()