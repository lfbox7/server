#!/usr/bin/python3


challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# My eyes! The goggles do nothing!

# challenge
print(f'My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!')

# trial
print(f"My {trial[2].get('goggles')}! The {trial[2].get('eyes')} do {trial[3]}!")

# nightmare
my_nightmare = nightmare[0]
print(f"My {my_nightmare['user']['name'].get('first')}! The {my_nightmare.get('kumquat')} do {my_nightmare.get('d')}! ")
