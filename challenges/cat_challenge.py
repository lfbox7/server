#!/usr/bin/python3

import requests
import random

url = 'https://cat-fact.herokuapp.com/facts'

def main():

    items = requests.get(f'{url}')
    print(items.headers)
    print(items.status_code)

    items = items.json()

    

    num = random.randrange(1, len(items), 1)
    print('Random cat fact: ')
    print(items[num]['text'])
    """
    for item in items:
        print(item['text'])
    """
if __name__ == '__main__':
    main()
