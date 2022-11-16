"""
Implement a program that prompts the user for items
Until the user closes using ctrl-c
Output the user's grocery list in all uppercase when they close app
Sorted Alphabetically by item

    1 APPLE
    2 BANANA
    1 ICE CREAM
    
    ^^ Example out output ^^
    
EOFError <-- The Exception you're gonna work with
KeyError <-- Error when something doesn't exist in dictionary
"""
groceries = {}

while True:
    try:
        item = input("")
        groceries[item.capitalize()] += 1
    except KeyError:
        groceries[item.capitalize()] = 1
    except (EOFError, KeyboardInterrupt):
        for item in sorted(groceries.keys()):
            print(f"{groceries[item]} {item}")
        break
