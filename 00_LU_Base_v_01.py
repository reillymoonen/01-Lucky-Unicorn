

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


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            responce = int(input(question))
            # if the amount is too low / too high give
            if low < responce <= high:
                return responce

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# Ask user how much they want to play with...
how_much = num_check("How much would you "
                     "like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))