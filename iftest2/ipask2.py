#!/usr/bin/env python3
"""
Alta3 Research | LFBox
Conditionals - testing if strings test true
"""

# prompt user for input
ipchk = input("Apply an IP address: ")

# check for gateway
if ipchk == '192.168.70.1':
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
# a provided string will test true
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)
# if no entry
else:
   print("You did not provide input.")
