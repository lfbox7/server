#!/usr/bin/env python3
"""
Alta3 Research | LFBox
Conditionals - Life of Brian guessing game using a while True loop.
"""

# counter for rounds
round = 0

while True:
    # increase rounds each time through loop
    round = round + 1
    # ask question
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    # prompt user for answer
    answer = input('Your guess--> ')
    # check user answer
    if answer == 'Brian':
        print('Correct')
        break
    elif round == 3:
        print('Sorry, the answer was Brian.')
        break;
    else:
        print('Sorry! Try again!')
