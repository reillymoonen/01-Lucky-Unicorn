import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0,100):
    chosen_num = random.choice(1, 100)

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5


print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance ${:.2f}".format(balance))