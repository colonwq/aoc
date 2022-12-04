#!/usr/bin/python3
import re
import numpy as np

IF = open("../day11.data")
#IF = open("../day11.example")
#IF = open("../day11.demo")
count = 0
mappoints = []
flashedpoints = []

maxgenerations = 100

for line in IF:

    line = line.rstrip("\r\n")
    #print("Line: %s (%d)" % ( line, len(line) ) )
    points = np.empty(len(line), dtype=int )
    flashpoints = np.empty(len(line), dtype=int )
    i = 0
    while i < len(line):
        #print( "Point: %d" % ( int(line[i]) ) )
        points[i] = int(line[i])
        flashpoints[i] = 0
        i += 1
    #print("Points: " , points )
    mappoints.append(points)
    flashedpoints.append( flashpoints )

rowLength = len(mappoints[0])
columnLength = len(mappoints)

allpoints = rowLength*columnLength
thesepoints = 0
print("The map is (%d x %d )" % (rowLength, columnLength ) )
for row in mappoints:
    print( row ) 

generation = 0
while thesepoints < allpoints:
    #increase everyone by 1
    #reset flashpoints
    thesepoints = 0
    i = 0
    while i < columnLength:
        j = 0
        while j < rowLength:
            mappoints[i][j] += 1
            flashedpoints[i][j] = 0
            j += 1
        i += 1

    #fire off and update as needed. 
    #we iterate until it stops rippiling
    hasFlashed = True
    while hasFlashed:
        i = 0
        hasFlashed = False
        while i < columnLength:
            j = 0
            while j < rowLength:
                if mappoints[i][j] > 9 and flashedpoints[i][j] != 1:
                    thesepoints += 1
                    hasFlashed = True
                    count += 1
                    #print("Point: [%d][%d] needs to flash" % ( i , j ) )
                    mappoints[i][j] = 0
                    flashedpoints[i][j] = 1
                    #bump up left
                    if i-1 >= 0 and j-1>=0 and flashedpoints[i-1][j-1] == 0:
                        #print( "bumping up left")
                        mappoints[i-1][j-1] += 1
                    #bump up
                    if i-1 >= 0 and flashedpoints[i-1][j] == 0:
                        #print( "bumping up")
                        mappoints[i-1][j] += 1
                    #bump up right
                    if i-1 >= 0 and j+1<=rowLength-1 and flashedpoints[i-1][j+1] == 0:
                        #print( "Bumping up right")
                        mappoints[i-1][j+1] += 1
                    #bump left
                    if j-1 >= 0 and flashedpoints[i][j-1] == 0:
                        mappoints[i][j-1] += 1
                    #bump right
                    if j+1 < rowLength and flashedpoints[i][j+1] == 0:
                        mappoints[i][j+1] += 1
                    #bump down left
                    if i+1 < columnLength and j-1 >= 0 and flashedpoints[i+1][j-1] == 0:
                        mappoints[i+1][j-1] += 1
                    #bump down
                    if i+1 < columnLength and flashedpoints[i+1][j] == 0:
                        mappoints[i+1][j] += 1
                    #bump down right
                    if i+1 < columnLength and j+1 < rowLength and flashedpoints[i+1][j+1] == 0:
                        mappoints[i+1][j+1] += 1

                j += 1
            i += 1
    #print("Map after %d generations" % ( generation ) )
    #for row in mappoints:
    #    print( row ) 
    #reset the flashers
    i = 0
    while i < columnLength:
        j = 0
        while j < rowLength:
            flashedpoints[i][j] = 0
            j += 1
        i += 1

    generation += 1

#print("Map after %d generations" % ( generation ) )
#for row in mappoints:
#    print( row ) 
print( "Generation: %d" % ( generation ) )
print( "Count: %d" % ( count ) )
exit()

