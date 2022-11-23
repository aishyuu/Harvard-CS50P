"""
Implement a program that
Expects the user to provide 2 command line arguments
    Name of existing csv file
    Name of new CSV file to write as output
        Columns have to be in order (first, last, house)

Converts input to that output
    Split name to be first and last name
    Assume each student has both a first and last name
    
If the user doesn't provide two command-line arguments
or if the first argument can't be read
    program should exit via sys.exit() with an error message
"""
import sys
import csv

def main():
    before, after = verify()
    writing(before, after)

def verify():
    try:
        if len(sys.argv) > 3:
            print("Too many arguments")
            raise ValueError
        elif len(sys.argv) < 3:
            print("Too few arguments")
            raise ValueError
    except ValueError:
        sys.exit()
    
    try:
        if not sys.argv[1].endswith(".csv"):
            print("First file does not end in .csv")
            raise ValueError
    except ValueError:
        sys.exit()
        
    try:
        open(sys.argv[2], "x")
    except FileExistsError:
        print("Output file already exists. Input a file that does not exist yet")
        sys.exit()
        
    return (sys.argv[1], sys.argv[2])

def writing(before, after):
    #Create the new file you want to output to
    with open(after, "a") as file:
        #open the csv of the file we want to copy from
        before_csv = csv.DictReader(open(before))
        #start writing into the new file
        writer = csv.DictWriter(file, fieldnames=['first','last','house'])
        #Write the header for the new file "first, last, house"
        writer.writeheader()
        next(before_csv)
        for line in before_csv:
            last, first = line["name"].split(",")
            writer.writerow({"first": first, "last": last, "house": line["house"]})
           
            
            
        
    
if __name__ == "__main__":
    main()