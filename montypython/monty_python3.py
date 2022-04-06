#!/usr/bin/python3
"""
Alta3 Research | LFBox
Conditionals - Life of Brian guessing game without a while True loop.
"""

# define and initialize variables
round = 0
answer = " "


while round < 3 and answer != "Brian":
    # increase round each time through loop
    round += 1
    # prompt user for answer
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    # check answer
    if answer == "Brian":
        print("Correct!")
    # check if tries are up
    elif round == 3:
        print("Sorry, the answer was Brian.")
    # got it wrong
    else:
        print("Sorry. Try again!")
