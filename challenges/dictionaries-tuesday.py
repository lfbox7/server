#!/usr/bin/env python3
'''
Alta3 Research | LFBox
Challenge Tuesday - Dictionaries
'''

def main():
    # prompt user of input
    char_name = input('Which character do you want to know about? (Starlord, Mystique, Hulk): ').title()
    char_stat = input('What statistic do you want to know about? (real name, powers, archenemy): ').lower()

    marvelchars = {
        "Starlord":
            {"real name": "peter quill",
             "powers": "dance moves",
             "archenemy": "Thanos"},

        "Mystique":
            {"real name": "raven darkholme",
             "powers": "shape shifter",
             "archenemy": "Professor X"},

        "Hulk":
            {"real name": "bruce banner",
             "powers": "super strength",
             "archenemy": "adrenaline"}
    }
    print(f"{char_name}'s {char_stat} is: {marvelchars.get(char_name).get(char_stat).title()}")

# calling main()
if __name__ == '__main__':
    main()
