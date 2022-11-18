"""
Implement a program that prompts the user for names
    One name per line
Do this until the suer inputs control d (sys.exit())

Assume the user will input at least one name

If there is only one name, output it like this
    Adieu, adieu, to Frank
    
However if there are more than name, output it like this
    Adieu, adieu, to Frank and John
    
    Adieu, adieu, to Frank, John, and Louisa
"""
#Start with an empty list and the basic starting phrase
name_list = []
phrase = "Adieu, adieu, to "

#Until the user decides to stop the program, keep going
while True:
    try:
        #Ask for name and append it to the list
        name = input("")
        name_list.append(name)
    #Once the user decides to quit using ctrl-c
    except (KeyboardInterrupt):
        #If the list only has one name
        if len(name_list) == 1:
            #Output that one person on the list
            phrase += name_list[0]
            print(phrase)
        #If there are more than one name
        else:
            #Iterate through the list
            for name in name_list:
                #Check if the index of said name is the last on the list
                if name_list.index(name) + 1 == len(name_list):
                    #If it is, add an "and {name}"
                    phrase += f"and {name}"
                #If it's not
                else:
                    #append to the string like normal
                    phrase += f"{name}, "
            #Print out the whole phrase and now you leave
            print(phrase)
            break