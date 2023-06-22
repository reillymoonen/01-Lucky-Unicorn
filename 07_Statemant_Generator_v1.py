
def statement_generator(statemant, decoration):

    sides = decoration * 3

    statemant = "{} {} {}".format(sides, statemant, sides)
    top_bottom = decoration * len(statemant)

    print(top_bottom)
    print(statemant)
    print(top_bottom)

    return ""


# Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()
statement_generator("Congratulations you got a Unicorn", "!")