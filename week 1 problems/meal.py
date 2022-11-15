"""
Suppose you're in a country where you...
    Eat breakfast between 7:00 and 8:00
    Eat Lunch between 12:00 and 13:00
    Eat Dinner between 18:00 and 19:00

Implement a program that prompts the user for a time
Outputs
    Breakfast time
    Lunch time
    Dinner time
If it's not time for a meal, don't output anything at all
Assume the users input is in 24 hour time as
    #:## or ##:##
Assume that the meal's time range is inclusive
    So it's either 7:00, 8:00, or in between any of those times
"""
#Approach: Convert hours into minutes and add with minutes
#Then we can check if it's in between two minute values rather than hours and minutes

def main():
    time = input("What time is it? ")
    minutes = convert(time)
    #Breakfast time (7am and 8am)
    if minutes >= 420 and minutes <= 480:
        print("breakfast time")
    #Lunch time (12pm and 1pm)
    elif minutes >= 720 and minutes <= 780:
        print("lunch time")
    #Dinner time (6pm and 7pm)
    elif minutes >= 1080 and minutes <= 1140:
        print("dinner time")
    

def convert(time):
    hrs, min = time.split(":")
    #Multiply hours by 60 min and adding with minutes
    return((int(hrs) * 60) + int(min))

if __name__ == "__main__":
    main()