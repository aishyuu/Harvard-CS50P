def main():
    phrase = input("Phrase: ")
    print(shorten(phrase))


def shorten(phrase):
    result = ""
    for letter in phrase:
        lower_letter = letter.lower()
        if lower_letter not in ("a", "e", "i", "o", "u"):
            result += letter

    return result


if __name__ == "__main__":
    main()
