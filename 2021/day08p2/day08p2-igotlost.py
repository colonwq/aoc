#!/usr/bin/python3
#import numpy as np
import re

#IF = open("../day08.data")
IF = open("../day08.example")
count = 0
for line in IF:
    number = ""
    line = line.rstrip("\r\n")
    #print("Line: %s" % ( line) )
    ( pre , post) = line.split(" | ")
    #print( "Post: %s"% post )
    for part in post.split(" "):
        if len(part) == 2:
            number += "1"
            count += 1
        if len(part) == 4:
            number += "4"
            count += 1
        if len(part) == 3:
            number += "7"
            count += 1
        if len(part) == 7:
            number += "8"
            count += 1
        #2 5 parts, 
        #3 5 parts, has both parts of 1 and extra of 7, extra part is A
        #5 5 parts
        #6 6 parts
        #9 6 parts
        #0 6 parts
    print( "Partial Number: %s" % ( number) )

print( "Count of 1, 4, 7, and 8: %d" % (count) )
