#!/usr/bin/python3.6
import numpy as np
import re

#IF = open("../day06.data")
IF = open("../day06.example")

population = []
generation = 0
maxGenerations = 256
#maxGenerations = 80
#maxGenerations = 18

line = IF.readline()
line = line.rstrip("\r\n")
line = re.sub(",", " ", line)
#population = re.split(" ", line)
for part in re.split(" ", line):
    population.append(int(part))

print("Population count: %d" % ( len( population ) ) )
#print("Initial state:" , population ) 

while generation < maxGenerations:
    i = 0
    startPopulation = len(population)
    #decrement day count
    while i < startPopulation:
        population[i] -= 1
        if population[i] < 0:
            population[i] = 6
            population.append(8)
        i += 1

    print("After %02d days: " % ( generation+1), len(population) ) 
    generation += 1
print("Population count: %d" % ( len( population ) ) )
