#!/usr/bin/python3.6
import numpy as np
import re

IF = open("../day06.data")
#IF = open("../day06.example")

population = []
generation = 0
maxGenerations = 256
#maxGenerations = 80
#maxGenerations = 18

line = IF.readline()
line = line.rstrip("\r\n")
line = re.sub(",", " ", line)
#population = re.split(" ", line)

# I need generation spots for 
# -1 0 1 2 3 4 5 6 7 8
populationlist = np.zeros( 10 )
print( "Empty Population List: ", populationlist )

for part in re.split(" ", line):
    #print("Found generation %d" % ( int(part) ) )
    populationlist[int(part) + 1] += 1

print( "Initial population list", populationlist )

while generation < maxGenerations:
    i = 0
    while i < populationlist.size - 1:
        populationlist[i] = populationlist[i+1]
        i += 1
    populationlist[9] = populationlist[0]
    populationlist[7] += populationlist[0]
    #print( "Next population list", populationlist )
    generation += 1

i = 1
total = 0
while i < populationlist.size:
    total += populationlist[i]
    i += 1
print("Population count: %d" % ( total ) )
