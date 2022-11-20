def main():
    greeting = input("Greeting: ")
    print(greet_check(greeting))


def greet_check(greeting):
    # Get the very first word of the phrase (lower case)
    stripped_greet = greeting.split()[0].lower()
    # If the first 5 letters are hello, return 0
    if stripped_greet[0:5] == "hello":
        return "$0"
    # If the first letter is 0, return 20
    elif stripped_greet[0] == "h":
        return "$20"
    # Anything else, return 100
    else:
        return "$100"


if __name__ == "__main__":
    main()
