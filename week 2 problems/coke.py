"""
Suppose a machine sells Coke bottles for 50 sents
The machine only accepts coins in: 25 cents, 10 cents, and 5 cents

Implement a program that prompts the user to insert a coin, one at a time
Each time informing the user of the amount due
Once the user inputted at least 50 cents, output how much change is owed

For example:
    Amount Due: 50
    Insert Coin: 25
    Amount Due: 25
    Insert Coin: 10
    Amount Due: 15
    Insert Coin: 10
    Amount Due: 5
    Insert Coin: 10
    Change Owed: 5
"""

def main():
    #Set the due amount and paid
    due = 50
    paid = 0
    
    #Set while loop until the full 50 cents is payed
    while due > 0:
        #Print out how much is due from the beginning
        print(f"Amount Due: {due}")
        #Make another for the user to input as many times needed
        while True:
            #Ask user to input int value
            paid = int(input("Insert Coin: "))
            #Checks if the int value is 25, 10, or 5
            if paid == 25 or paid == 10 or paid == 5:
                break
        #Subtract the input from the amount due
        due -= paid
    #At the end, multiply the due by -1 to get a positive owed value
    print(f"Change Owed: {due * -1}")

main()