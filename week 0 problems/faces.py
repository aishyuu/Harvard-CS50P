# Replaces the emoticon with the proper emoji
def convert(userInput):
    userInput = userInput.replace(":)", "🙂")
    userInput = userInput.replace(":(", "🙁")
    return userInput

#Get input from user
userInput = input()

#Print the converted userInput
print(f"{convert(userInput)}")