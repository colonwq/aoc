#!/usr/bin/python3.6

IF = open("day1.data")
last = -1
increase = 0

for line in IF:
    #print(line)
    depth = int(line)
    if depth > last and last != -1:
        increase += 1
    last = depth

print( "Number of increases: %d " % ( increase ) )
