"""
Implement a program that takes exactly one command line argument
    A CSV file
Output a table formatted in ASCII art
    Use Tabulate
Format the table using the grid format
    Also on tabulate I think
If the name doesn't end in .csv, or it doesn't exist...
    sys.exit()
"""

from tabulate import tabulate
import sys

def main():
    verify()
    chart(sys.argv[1])

def chart(csv_file):
    with open(csv_file) as file:
        head = file.readline()
        print(tabulate(file, head, tablefmt="grid"))
        
def verify():
    try:
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            raise ValueError
        elif len(sys.argv) < 2:
            print("Too few command-line arguments")
            raise ValueError
        if not sys.argv[1].endswith(".csv"):
            raise ValueError
        open(sys.argv[1])
        
    except ValueError:
        sys.exit()
    except FileNotFoundError:
        print("File does not exist")
        sys.exit()
        
        
if __name__ == "__main__":
    main()