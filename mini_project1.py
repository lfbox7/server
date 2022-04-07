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

def title():
    print(' ______     ______     ______     ______   ______')
    print('/\  ___\   /\  == \   /\  __ \   /\  == \ /\  ___\\')
    print('\ \ \____  \ \  __<   \ \  _  \  \ \  _-/ \ \___  \\')
    print(' \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_\    \/\_____\\')
    print('  \/_____/   \/_/ /_/   \/_/\/_/   \/_/     \/_____/\n\n')


def welcome():
    print('__          __  _                            _          _   _            _        _     _')
    print('\ \        / / | |                          | |        | | | |          | |      | |   | |')
    print(' \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___  | |_ __ _| |__ | | ___')
    print("  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \ | __/ _` | '_ \| |/ _ \\")
    print('   \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | || (_| | |_) | |  __/')
    print('    \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___|  \__\__,_|_.__/|_|\___|')


def keep_rolling():
    print(' _  __                           _ _ _')
    print('| |/ /                          | | (_)')
    print("| ' / ___  ___ _ __    _ __ ___ | | |_ _ __   __ _")
    print("|  < / _ \/ _ \ '_ \  | '__/ _ \| | | | '_ \ / _` |")
    print('| . \  __/  __/ |_) | | | | (_) | | | | | | | (_| |')
    print('|_|\_\___|\___| .__/  |_|  \___/|_|_|_|_| |_|\__, |')
    print('              | |                             __/ |')
    print('              |_|                            |___/')


def win():
    print('__     __          __          ___')
    print('\ \   / /          \ \        / (_)')
    print(' \ \_/ /__  _   _   \ \  /\  / / _ _ __')
    print("  \   / _ \| | | |   \ \/  \/ / | | '_  \\")
    print('   | | (_) | |_| |    \  /\  /  | | | | |')
    print('   |_|\___/ \__,_|     \/  \/   |_|_| |_|\n\n')


def craps():
    print('  _____')
    print(' / ____|')
    print('| |     _ __ __ _ _ __  ___')
    print("| |    | '__/ _` | '_ \/ __|")
    print('| |____| |  | (_ | |_) \__ \\')
    print(' \_____|_|  \__,_| ,__/|___/')
    print('                 | |')
    print('                 |_|\n\n')



def lose():
    print('__     __           _')
    print('\ \   / /          | |')
    print(' \ \_/ /__  _   _  | |      ___  ___  ___')
    print('  \   / _ \| | | | | |     / _ \/ __|/ _ \\')
    print('   | | (_) | |_| | | |____| (_) \__ \  __/')
    print('   |_|\___ /\__,_| |_______\___/|___/\___|\n\n')


def game_over():
    print(' _____          __  __ ______    ______      ________ _____')
    print('/ ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \\')
    print('| |  __  /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |')
    print('| | _ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  /')
    print('| |_| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \\')
    print('\_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\\')


def one():
    print(' _______')
    print('|       |')
    print('|   0   |')
    print('|       |')
    print(' _______')


def two():
    print(' _______')
    print('|   0   |')
    print('|       |')
    print('|   0   |')
    print(' _______')


def three():
    print(' _______')
    print('|   0   |')
    print('|   0   |')
    print('|   0   |')
    print(' _______')


def four():
    print(' _______')
    print('| 0   0 |')
    print('|       |')
    print('| 0   0 |')
    print(' _______')


def five():
    print(' _______')
    print('| 0   0 |')
    print('|   0   |')
    print('| 0   0 |')
    print(' _______')


def six():
    print(' _______')
    print('| 0   0 |')
    print('| 0   0 |')
    print('| 0   0 |')
    print(' _______')


def print_result(die):

    if die == 1:
        one()
    elif die == 2:
        two()
    elif die == 3:
        three()
    elif die == 4:
        four()
    elif die == 5:
        five()
    else:
        six()


def throw_dice():
    print('\n\nThrowing the dice...')
    die1 = random.randrange(1, 6, 1)
    die2 = random.randrange(1, 6, 1)
    print_result(die1)
    print_result(die2)
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
        lose()
        main(False, False)
    elif result == point:
        win()
        main(True, False)


def come_out_roll_results():
    result = throw_dice();
    if result == 7 or result == 11:
        win()
        main(True, False)
    elif result == 2 or result == 3 or result == 12:
        craps()
        lose()
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
        main(False, False)


def main(keep_playing, come_out_roll):
    if keep_playing and come_out_roll:
        title()
        welcome()
        get_result(come_out_roll)
    elif keep_playing and not come_out_roll:
        keep_rolling()
        get_result(True)
    else:
        game_over()
        quit()


if __name__ == '__main__':
    main(True, True)    

