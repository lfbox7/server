#!/usr/bin/python3

from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] 
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice

def main():
    """called at run time"""

    player1 = Player()
    player2 = Player()

    player1.roll()
    player2.roll()

    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw!")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == "__main__":
    main()

