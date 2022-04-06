#!/usr/bin/env python3
"""
Alta3 Research || LFBox
Check hostname against expected value
"""

def main():
    """
    Checking hostname against input
    """

    # Collect input from user
    hostname = input("What value should we set for hostname?")

    # use the lower method to test if input value matches expected value
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")

    # Always print out to the user
    print("Exiting the script")

# calling main()
if __name__ == '__main__':
    main()
