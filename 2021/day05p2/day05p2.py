#!/usr/bin/python3.6
import numpy as np
import re

IF = open("../day05.data")
#IF = open("../day05.example")

maxX = 0
maxY = 0
mappoints = []

for line in IF:
    line = line.rstrip("\r\n")
    line = re.sub(",|-|>", " ", line)
    line = re.sub(" +", " ", line )
    #print( "Line: %s" % (line) )
    [x1, y1, x2, y2 ] = re.split(" ", line)
    #print( "The number of parts: %d" % (len(parts)))
    maxX = max( maxX, max( int(x1), int(x2)) )
    maxY = max( maxY, max( int(y1), int(y2)) )
    mappoints.append([int(x1), int(y1), int(x2), int(y2) ])

maxXY = max( maxX, maxY )
print("Max X: %d" % ( maxX ) )
print("Max Y: %d" % ( maxY ) )

floormap = np.empty([maxXY+1, maxXY+1], dtype=int)
i = j = -1
while i < maxXY:
    while j < maxXY:
        floormap[i+1][j+1] = 0
        j += 1
    j = -1
    i += 1

#print("Empty map")
#print( floormap )

print("Adding points")

for [x1, y1, x2, y2] in mappoints:
    #print("Points: ", [x1, y1, x2, y2])
    if x1 == x2:
        #print("Virticle line [%d, %d] -> [%d, %d]" % (x1, y1, x2, y2) )
        ystart = min(y1, y2)
        yend   = max(y1, y2)
        while ystart <= yend:
            #floormap[x1,ystart] += 1
            floormap[ystart, x1] += 1
            ystart += 1
        #print( floormap )
        continue 
    if y1 == y2:
        #print("Horizontal line [%d, %d] -> [%d, %d]" % (x1, y1, x2, y2) )
        xstart = min(x1, x2)
        xend   = max(x1, x2)
        while xstart <= xend:
            #floormap[xstart, y1] += 1
            floormap[y1, xstart] += 1
            xstart += 1
        #print( floormap )
        continue 
    if x2 < x1:
        #print("Backwards line... switching points [%d, %d] -> [%d, %d]" % (x1, y1, x2, y2))
        xTemp = x1
        yTemp = y1
        x1 = x2
        y1 = y2
        x2 = xTemp
        y2 = yTemp
        #print("Switched points [%d, %d] -> [%d, %d]" % (x1, y1, x2, y2))
        #print("Differences X: %d Y %d" % (x1-x2, y1-y2) )
    if y2 < y1:
        #print("Slopes 'up' [%d, %d] -> [%d, %d]" % (x1, y1, x2, y2))
        xstart = x1
        ystart = y1
        while xstart <= x2:
            floormap[ystart, xstart] += 1
            xstart += 1
            ystart -= 1
        continue
    if y2 > y1:
        #print("Slopes 'down' [%d, %d] -> [%d, %d]" % (x1, y1, x2, y2))
        xstart = x1
        ystart = y1
        while xstart <= x2:
            floormap[ystart, xstart] += 1
            xstart += 1
            ystart += 1
        

    #print("next")

#print( floormap )

count = 0
for row in floormap:
    for cell in row:
        if cell > 1:
            count += 1

        

print( "Avoid count: %d" % (count) )
