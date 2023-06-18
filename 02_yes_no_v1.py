
# Functions go here...
def yes_no(questions):
    valid = False
    while not valid:
        responce = input("Have you played this game "  
                         "before?").lower()

        if responce == "yes" or responce == "y":
                responce = "yes"
                return responce

        elif responce == "no" or responce == "n":
                responce = "no"
                return responce

        else:
            print("Please answer yes / no")

# Main Routine goes here...

show_instructions = yes_no("Have you played the "
                                "game before?")
print("You choose {}".format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("You said {} to having fun".format(having_fun))
