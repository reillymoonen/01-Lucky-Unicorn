# Functions go here
def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            responce = int(input("How much would you "
                                 "like to play with? "))
            # if the amount is too low / too high give
            if 0 < responce <= 10:
                print("You have asked to play "
                      "with ${}".format(responce))

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)
# Main routine goe here



# Print the