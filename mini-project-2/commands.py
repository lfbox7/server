import random
from room_dict import rooms
from character_dict import characters
from equipment_dict import equipment


def go(current_room, room):
    if room in rooms[current_room]:
        return rooms[current_room][room]
    else:
        print('You can\'t go that way!')
        return current_room


def look(current_room, direction):
    if direction in rooms[current_room]['look']:
        print(rooms[current_room]['look'].get(direction))
    else:
        print('Nothing to see here.')


def get(current_room, named_item):
    if "item" in rooms[current_room] and named_item in rooms[current_room]['item']:
        # add the item to their inventory
        characters['hero']['inventory'].append(named_item)
        # display a helpful message
        print(named_item.title() + ' retrieved!')
        # delete the item from the room
        del rooms[current_room]['item']
        equipment[named_item]['location'] = 'hero'
    # otherwise, if the item isn't there to get
    else:
        # tell them they can't get it
        print('Can\'t get ' + named_item + '!')


def use(named_item):
    if named_item in characters['hero']['inventory'] and characters['hero']['use'] is None:
        if named_item == 'potion':
            health = characters['hero']['health']
            modifier = random.randint(10, 25)
            characters['hero']['health'] = health + modifier
            characters['hero']['inventory'].remove(named_item)
        else:
            characters['hero']['use'] = named_item
            characters['hero']['inventory'].remove(named_item)
            print('You can now use the ' + named_item + '.')
    elif characters['hero']['use'] is not None:
        print('You cannot use the ' + named_item + ', you are holding a ' + characters['hero'].get('use') + '.')
    else:
        print('There is not a ' + named_item + ' in your inventory.')


def drop(current_room, named_item):
    if named_item in characters['hero']['inventory']:
        print('You cannot drop an item from your inventory.\nYou must use item first!')
        return
    if named_item in characters['hero']['use']:
        rooms[current_room]['item'] = named_item
        characters['hero']['use'] = None
        print('You dropped the ' + named_item + ' in the ' + current_room + '.')
    else:
        print('You are currently not using any items.')


def ask(character):
    if characters[character]['answer'] is not None:
        print(characters[character].get('answer'))
    else:
        print('Sorry, I am an NPC.')


def attack(current_room, character):
    if character == 'butler':
        print('Sorry I offended you, sir!')
        return 'You may not attack an NPC.'
    if character == 'princess':
        print('You are supposed to save me! Not KILL me!')
        return 'You may not attack the princess.'
    hero_modifier = 1
    if character == 'ogre' and current_room == 'servant\'s quarters':
        if characters['hero'].get('use') is None:
            hero_modifier = .5
        elif characters['hero'].get('use') == 'sword':
            hero_modifier = 2
        elif characters['hero'].get('use') == 'dagger':
            hero_modifier = 1
        else:
            print('You cannot attack with a ' + characters['hero'].get('use') + '.')
        battle(hero_modifier)
        del rooms[current_room]['character']
        del rooms['solar']['character']
        temp = ['ogre', 'princess']
        rooms['garden']['character'] = temp
        print('After attacking the ogre, she fled and grabbed the princess!')
    elif character == 'ogre' and current_room == 'garden':
        if characters['hero'].get('use') is None:
            hero_modifier = .5
        elif characters['hero'].get('use') == 'sword':
            hero_modifier = 2
        elif characters['hero'].get('use') == 'dagger':
            hero_modifier = 100
        else:
            print('You cannot attack with a ' + characters['hero'].get('use') + '.')
        battle(hero_modifier)


def battle(hero_modifier):
    hero_strength = characters['hero'].get('strength')
    hero_health = characters['hero'].get('health')
    ogre_strength = characters['ogre'].get('strength')
    ogre_health = characters['ogre'].get('health')
    ogre_modifier = random.randint(5, 9)
    characters['hero']['health'] = hero_health - (ogre_strength * ogre_modifier)
    characters['ogre']['health'] = ogre_health - (hero_strength * hero_modifier)
    if characters['ogre']['health'] < 0:
        print('You killed the ogre!')
        print('You saved the princess')
        print('GAME OVER')
        quit()
    elif characters['hero']['health'] < 0:
        print('You failed in your quest!')
        print('GAME OVER')
        quit()

    else:
        print('You inflicted ' + str(ogre_strength * ogre_modifier) + ' and suffered ' + str(hero_strength * hero_modifier) + ' damage.')


