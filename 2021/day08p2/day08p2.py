#!/usr/bin/python3
#import numpy as np
import re

#IF = open("../day08.data")
IF = open("../day08.example")

segment_map = {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        }

for line in IF:
    values = {
            "0": [],
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
            }
    line = line.rstrip("\r\n")
    #print("Line: %s" % ( line) )
    (inputs , output) = line.split( " | ")
    #print( "Input: %s" % (inputs) )
    #print( "Output: %s" % (output) )
    count = 0
    for input in inputs.split(" "):
        count += 1
        if len(input) == 2:
            #print("Input:%s"% ( input) )
            #print("Found a 1 (%s)" % (input) )
            values["1"].append(input) 
        elif len(input) == 4:
            #print("Found a 4 (%s)" % (input) )
            values["4"].append(input) 
        elif len(input) == 3:
            #print("Found a 7 (%s)" % (input) )
            values["7"].append(input) 
        elif len(input) == 7:
            #print("Found an 8 (%s)" % (input) )
            values["8"].append(input) 
        elif len(input) == 5:
            values["5"].append(input) 
            print("Found a 2, 3, or 5 (%s)" % (input) )
        elif len(input) == 6:
            values["6"].append(input) 
            #print("Found a 6, 9, or 0 (%s)" % (input) )
        else:
            print("Input:%s"% ( input) )
    #print( "Total found: %d" % (count) )
    print( "Current map ", values )

    # find the A segment (7 - 1)
    #print("1 Parts: %s" % ( values["1"]) )
    #print("7 Parts: %s" % ( values["7"]) )
    seg_1 = set(values["1"][0])
    for test in set(values["7"][0]):
   #     print("Looking for %s in 1" %( test) )
        if test not in seg_1:
            segment_map["a"] = test
    print( "Segment map after A: ", segment_map )

    # find E
    # BEF is the changing part of 2, 3, 5

