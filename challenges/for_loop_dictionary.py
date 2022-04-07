#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "SW Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NW Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}
         ]

farm_input = input('Choose a farm (NE Farm, NW Farm, East Farm, West Farm, SE Farm, or SW Farm): ').lower()
agriculture_input = input("Choose the farm's product (Animal or Produce): ").lower()

if farm_input.startswith('e'):
    farm_input = 'east farm'
elif farm_input.startswith('w'):
    farm_input = 'west farm'

agri_list = []
if agriculture_input == 'animal':
    agri_list = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]
else:
    agri_list = ["carrots", "celery", "bananas", "apples", "oranges"]

results = []
for farm in farms:
    if farm['name'].lower() == farm_input:
        for agri in farm['agriculture']:
            if agri in agri_list:
                results.append(agri)
if len(results) == 0:
    print('Sorry no results')
else:
    print(f'The {agriculture_input}s at {farm_input} is {", ".join(results)}.')
