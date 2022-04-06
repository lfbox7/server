#!/usr/bin/env python3
"""
Alta3 Research | LFBox
Mini-project 1
"""

import random

"""
1st roll 
    win on 7 or 11
    lose on 2,3, or 12
    point otherwise 4,5,6,8,9,10
Next rolls
    lose 7 - end game new shooter
    win get the point - reset game with same shooter
    any other number - keep rolling
"""


def throw_dice():
    print('Throw the dice!')
    die1 = random.randrange(1, 6, 1)
    die2 = random.randrange(1, 6, 1)
    print(f'You rolled a {die1 + die2}')
    return die1 + die2


def point_roll(point):
    result = 0
    while True:
        result = throw_dice()
        if result == 7:
            break
        elif result == point:
            break
    if result == 7:
        print('Sorry! You Lose!')
        main(False, False)
    elif result == point:
        print('You win!')
        main(True, False)


def come_out_roll_results():
    result = throw_dice();
    if result == 7 or result == 11:
        print('You win!')
        main(True, False)
    elif result == 2 or result == 3 or result == 12:
        print('Sorry! You lose!')
        main(False, False)
    else:
        return result


def get_result(come_out_roll):
    point = 0
    if come_out_roll:
        point = come_out_roll_results()
    if point != 0:
        point_roll(point)
    else:
        main(False, False, 0)


def main(keep_playing, come_out_roll):
    if keep_playing and come_out_roll:
        print('Welcome to the table.')
        get_result(come_out_roll)
    elif keep_playing and not come_out_roll:
        print("Let's continue!")
        get_result(True)
    else:
        print('GAME OVER')


if __name__ == '__main__':
    main(True, True)

