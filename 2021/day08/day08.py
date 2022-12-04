#!/usr/bin/python3
#import numpy as np
import re

IF = open("../day08.data")
#IF = open("../day08.example")
count = 0

for line in IF:

    line = line.rstrip("\r\n")
    #print("Line: %s" % ( line) )
    ( pre , post) = line.split(" | ")
    #print( "Post: %s"% post )
    for part in post.split(" "):
        if len(part) == 2:
            count += 1
        if len(part) == 3:
            count += 1
        if len(part) == 4:
            count += 1
        if len(part) == 7:
            count += 1
print( "Count of 1, 4, 7, and 8: %d" % (count) )
