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
population = re.split(" ", line)
#for part in re.split(" ", line):
#    population.append(int(part))
populationlist = np.zeros(len(population))
print("Population count: %d" % ( len( population ) ) )
print("Population listcount: %d" % ( populationlist.size ) )
i = 0
while i < len(population):
    populationlist[i] = int(population[i])
    i += 1

#print( populationlist )
print("Initial state: " , populationlist ) 

while generation < maxGenerations:
    i = 0
    startPopulation = populationlist.size
    #decrement day count
    while i < startPopulation:
        populationlist[i] -= 1
        if populationlist[i] < 0:
            populationlist[i] = 6
            arr = np.array([8], dtype=int )
            populationlist = np.concatenate(( populationlist, arr ))
        i += 1

    print("After %02d days: " % ( generation+1), populationlist ) 
    #print("After %02d days: " % ( generation+1), populationlist.size ) 
    generation += 1
print("Population count: %d" % ( populationlist.size ) )
