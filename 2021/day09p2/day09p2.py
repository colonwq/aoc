#!/usr/bin/python3
import re
import numpy as np

IF = open("../day09.data")
#IF = open("../day09.example")
count = 0
mappoints = []
bottompoints = []

basinsize = []

def sumbasin( x, y ):
    subsum = 1
    #print("Current mount point value: %d" % ( mappoints[ x ][ y] ))

    if mappoints[ x ][ y] >= 9:
        return 0

    mappoints[ x ][ y] = 9
    #print( "Column: %d Row: %d" % ( x, y) )
    if x > 0:
        subsum += sumbasin( x - 1, y)
    if x + 1 < columnLength:
        subsum += sumbasin( x + 1, y)

    if y > 0:
        subsum += sumbasin( x, y - 1)
    if y+1 < rowLength:
        subsum += sumbasin( x, y + 1)
    return subsum

for line in IF:

    line = line.rstrip("\r\n")
    #print("Line: %s (%d)" % ( line, len(line) ) )
    points = np.empty(len(line), dtype=int )
    i = 0
    while i < len(line):
        #print( "Point: %d" % ( int(line[i]) ) )
        points[i] = int(line[i])
        i += 1
    #print("Points: " , points )
    mappoints.append(points)

#for points in mappoints:
#    print( points )

rowLength = len(mappoints[0])
columnLength = len(mappoints)

print("The map is (%d x %d )" % (rowLength, columnLength ) )

j = 0

while j < columnLength:
    bottompoints.append( np.zeros(rowLength, dtype=(int) ) )
    j += 1

i = 0
while i < columnLength:
    j = 0
    while j < rowLength:
        up = down = left = right = 0
        foundup = founddown = foundleft = foundright = 0
        #print("Looking at (%d, %d): %d" % (i,j, mappoints[i][j] ) )
        if i - 1 >= 0:
            #print(" Test left [%d, %d] %d" % (i-1, j, mappoints[i-1][j] ) )
            if mappoints[i][j] < mappoints[i-1][j]:
                left = 1
                foundleft = mappoints[i-1][j]
        else:
            #print(" Test left [%d, %d] %d" % (i-1, j, -1 ) )
            left = 1
            foundleft = -1
        if j + 1 < rowLength:
            #print(" Test right [%d, %d] %d" % (i, j+1, mappoints[i][j+1] ))
            if mappoints[i][j] < mappoints[i][j+1]:
                right = 1
                right = mappoints[i][j+1]
        else:
            #print(" Test right [%d, %d] %d" % (i, j+1, -1 ))
            right = 1
            right = -1
        if j - 1 >= 0:
            #print(" Test up [%d, %d] %d" % (i, j-1, mappoints[i][j-1]) )
            if mappoints[i][j] < mappoints[i][j-1]:
                up = 1
                up = mappoints[i][j-1]
        else:
            #print(" Test up [%d, %d] %d" % (i, j-1, -1 ) )
            up = 1
            up = -1
        if i + 1 < columnLength:
            #print(" Test down [%d, %d] %d" % (i+1,j, mappoints[i+1][j] ))
            if mappoints[i][j] < mappoints[i+1][j]:
                down = 1
                down = mappoints[i+1][j]
        else:
            #print(" Test down [%d, %d] %d" % (i+1,j, -1 ))
            down = 1
            down = -1
        if down and left and up and right:
            #print("Found a low spot (%d, %d) -> %d" % ( i, j, mappoints[i][j] ) )
            #print("Left: %d Right: %d Up: %d Down: %d" % (foundleft, foundright, foundup, founddown ) )
            bottompoints[i][j] = 1

        j += 1
    i += 1



#print( bottompoints )
#for row in bottompoints:
#    print( row ) 

danger = 0
i = 0
while i < columnLength:
    j = 0
    while j < rowLength:
        if bottompoints[i][j] > 0:
            basinsize.append( sumbasin(i, j ) )
        j += 1
    i += 1
basinsize.sort(reverse=True)
print("Number of basins: %d" % ( len(basinsize) ))
print("Basin depths: " , basinsize )
answer = basinsize[0] * basinsize[1] * basinsize[2]
print("Answer: %d" % ( answer ) )
