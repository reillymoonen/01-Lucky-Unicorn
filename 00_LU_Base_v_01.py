

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

def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main Routine goes here...
played_before = yes_no("Have you played the "
                                "game before?")

if played_before == "no":
    instructions()

print("Program continues")
