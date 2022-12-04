#!/usr/bin/python3
'''
  Day 12 part 1
'''
import re
#import numpy as np

IF = open("../day12.data")
#IF = open("../day12.large")
#IF = open("../day12.medium")
#IF = open("../day12.small")

MAP = {}
CURPATH = []

def process_room(curroom):
    '''
    Take the current room. Find the next room. wash..rense.. repeat
    '''
    global PATH_COUNT
    #print("Processing room: %s"%(curroom))
    connected_rooms = MAP[curroom]
    #print("Connected rooms: %s"%(connected_rooms))
    rooms = re.split(":", connected_rooms)
    #print("Rooms list: ", rooms)
    for room in rooms:
        if room == "end":
            CURPATH.append(room)
            #print("Found the exit ", CURPATH)
            PATH_COUNT += 1
            CURPATH.pop()
        else:
            if room.islower() and room in CURPATH:
                print("Already visted room: %s"%(room))
                #print("Current path ", CURPATH)
            else:
                #print("Adding room %s to the current path"%(room))
                CURPATH.append(room)
                process_room(room)
                CURPATH.pop()


for line in IF:
    line = line.rstrip("\r\n")
    (From, To) = line.split("-")
    #print("From: %s To: %s" % (From, To))

    if From not in MAP.keys():
        #print("Add room: %s" % (From))
        MAP[From] = To
    else:
        MAP[From] += ":"
        MAP[From] += To

    if To not in MAP.keys():
        #print("Add room: %s" % (To))
        MAP[To] = From
    else:
        MAP[To] += ":"
        MAP[To] += From


#for key, value in MAP.items():
#    print("Rooms connected to %s: %s" % (key, value))

PATH_COUNT = 0
CURPATH.append("start")
process_room("start")

print("Total Paths Found: %d"%(PATH_COUNT))
