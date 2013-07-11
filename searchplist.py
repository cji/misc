#!/usr/bin/env python
#########################
# searchplist.py
# Usage: ./searchplist.py example.plist
#
# Allows you to search a plist for certain keys and output the value
# If there are nested plists stored as Data objects, it will extract the plist and output the value
# as well as save the nested plist to a new file.
# REQUIRES biplist Library
#
#########################

from biplist import *
import sys

try:
    plist = readPlist(sys.argv[1])
except:
    print 'Not a valid plist. Usage: ./searchplist.py example.plist'
    sys.exit()

while True:
    search = raw_input("Key Name Search (Q to quit): ").strip()
    if search.lower() == 'q':
        break

    results = 0

    for keys in plist:
        if search in keys:
            if isinstance(plist[keys], Data):
                plist_temp = readPlistFromString(plist[keys])
                writePlist(plist_temp, keys + '.plist')
                print '[+] Match: ' + keys
                print '[+] Value: ' + str(plist_temp)
                print '[*] Key contained a nested plist. File saved as: ' + keys + '.plist'
                print
            else:
                print '[+] Match: ' + keys
                print '[+] Value: ' + str(plist[keys])
                print
            results += 1
    if results == 0:
        print '[-] No matches found.'
        print
