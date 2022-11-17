"""
Implement a program that prompts the user for a date
In month-date-year order
Formatted like . . .

    9/8/1636
    or
    September 8, 1636

Wherein month in the latter can be any in the list below

Output the same date in YY-MM-DD format
If the input is not valid, prompt the user again
Assume every month has no more than 31 days
Don't validate whether a month has 28, 29, 30, or 31 days
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    print(f"{date()}")

def date():
    while True:
        try:
            date = input("Date: ")
            if "," in date:
                modified_date = date.replace(",", "").split()
                if modified_date[0] not in months:
                    death = 1/0
                elif int(modified_date[1]) > 31 or int(modified_date[1]) < 1:
                    death = 1/0
                else:
                    modified_date[0] = int(months.index(modified_date[0])) + 1
                    return(f"{modified_date[2]}-{modified_date[0]:0>2}-{modified_date[1]:0>2}")
            elif "/" in date:
                modified_date = date.replace("/", " ").split()
                return(f"{modified_date[2]}-{modified_date[0]:0>2}-{modified_date[1]:0>2}")
        except ZeroDivisionError:
            pass

main()