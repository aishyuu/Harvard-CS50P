"""
Implement a file that enables the user to place an order
Until the user inputs ctrl-c (exits program)
After each item, display the total cost, prefixed with "$"
Treat the users input case insensitively
Ignore any input that isn't an item
Assume every item on the menu will be titlecased <-- Use titlecase function
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#The error you're going to be using is KeyError
total = 0
while True:
    try:
        item = input("Item: ")
        total += menu[item.lower().title()]
        print(f"Total ${format(total, '.2f')}")
    except KeyError:
        pass
        
    