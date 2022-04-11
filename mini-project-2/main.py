#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live
import commands
from room_dict import rooms
from character_dict import characters


def show_instructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  look [direction]
  get [item]
  use [item]
  drop [item]
  ask [character]
''')


def show_status():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + current_room + '.')
    print('Your current health is ' + str(characters['hero'].get('health')) + ' of 100.')
    if characters['hero'].get('use') is None:
        print('You are not using any item.')
    else:
        print('You are using a ' + characters['hero'].get('use') + '.')
    # print the current inventory
    print('Inventory : ' + str(characters['hero'].get('inventory')) + '.')
    # print an item if there is one
    if 'item' in rooms[current_room]:
        print('You see a ' + rooms[current_room]['item'] + '.')
    if 'character' in rooms[current_room]:
        print('You see a ' + str(rooms[current_room]['character']) + ' in the ' + current_room + ' with you.')
    if message is not None:
        print(message)
    print("---------------------------")


# start the player in the Hall
current_room = 'entry'
message = None

show_instructions()

# loop forever
while True:

    show_status()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        current_room = commands.go(current_room, move[1])

    if move[0] == 'look':
        commands.look(current_room, move[1])

    # if they type 'get' first
    if move[0] == 'get':
        commands.get(current_room, move[1])

    if move[0] == 'use':
        commands.use(move[1])

    if move[0] == 'drop':
        commands.drop(current_room, move[1])

    if move[0] == 'ask':
        commands.ask(move[1])

    if move[0] == 'attack':
        commands.attack(current_room, move[1])
