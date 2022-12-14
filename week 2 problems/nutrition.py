"""
Implement a program that asks users to input a fruit (case-insensitively)
Output the number of calories is in one portion of the fruit
"""
fruits = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydew melon" : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "60",
    "orange" : "80",
    "peach" : "60",
    "pear" : "100",
    "pineapple" : "50",
    "plums" : "70",
    "strawberries" : "50",
    "sweet cherries" : "100",
    "tangerine" : "50",
    "watermelon" : "80"
}

def main():
    # Verify if the user writes something that's in the dict
    while True:
        user_fruit = input("Item: ")
        if user_fruit.lower() in fruits:
            break
    
    #Print the result
    print(f"Calories: {fruits[user_fruit.lower()]}")

main()