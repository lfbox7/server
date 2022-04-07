#!/usr/bin/env python3

import random

def apigrabber():
    status_codes= [200, 302, 307, 401, 403, 404, 418, 502]
    x= random.choice(status_codes)

    return x

def main():
    # all of your code will be written in the main function!
    x = apigrabber()
    print(f'Status code: {x}')
    if x >= 500:
        print('We done screwed up, son!')
    elif x >= 400:
        print('You done screwed up, son!')
    elif x >= 300:
        print('Redirecting')
    else:
        print('OK!')

main()
