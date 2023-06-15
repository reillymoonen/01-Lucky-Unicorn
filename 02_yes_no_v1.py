

# Functions go here...
def yes_no(questions):
    valid = False
    while not valid:
        responce = input("Have you played this game" 
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

show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game" "before?").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If answer is invalid, print an error.
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print("display_insructions")

    else:
        print("Please answer yes / no")
