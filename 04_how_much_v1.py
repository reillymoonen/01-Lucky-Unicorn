# Functions go here


# Main routine goe here

error = "Please enter an whole number beetween 1 and 10"

valid = False
while not valid:
    # ask the question
    responce = int(input("How much would you "
                   "like to play with?"))
    # if the amount is too low / too high give
    if 0 < responce <= 10:
        print("You have asked to play "
              "with ${}".format(responce))

    # output an error
    else:
        print(error)