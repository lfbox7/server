#!/usr/bin/python3

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def name_finder(got_list):
    names = []
    for x in got_list:
        r = requests.get(x)
        decodedjson = r.json()
        names.append(decodedjson.get("name"))
    return names

def main():
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        print("This character belongs to the following houses:")
        for x in name_finder(got_dj.get("allegiances")):
            print(x)
        print("This character appears in the following books:")
        for x in name_finder(got_dj.get("books")):
            print(x)

if __name__ == "__main__":
    main()

