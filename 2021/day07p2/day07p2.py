#!/usr/bin/python3.6
import numpy as np
import re

IF = open("../day07.data")
#IF = open("../day07.example")

line = IF.readline()
line = line.rstrip("\r\n")
line = re.sub(",", " ", line)
crabs = re.split(" ", line)

minfuel = -1
maxcrab = 0

for crab in crabs:
    maxcrab = max( maxcrab, int(crab) )

print("Farthest crab: %d" % (maxcrab) )

i = 1
testfuel = 0

while i <= maxcrab:
    #print("Testing step %d of %d. Minfuel: %d" % ( i, maxcrab, minfuel ) )
    for crab in crabs:
        steps = 0
        steps += abs(i - int(crab) )
        j = 1
        while j <= steps:
            testfuel += j
            j += 1
    #print("Test fuel: %d" % (testfuel) )
    if minfuel >= 0:
        minfuel = min( minfuel, testfuel ) 
    else:
        minfuel = testfuel
    i += 1
    testfuel = 0

print("Minimal fuel: %d" % ( minfuel ) )

