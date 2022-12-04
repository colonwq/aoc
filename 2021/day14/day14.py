#!/usr/bin/python3
'''
  Day 14 part 1
'''
import re
#import numpy as np

IF = open("../day14.data")
#IF = open("../day14.demo")

POLY = []
MAP = {}
MODE = 0
MAX_GEN = 10
COUNTS = {}

def process_gen():
    '''
    Grow polymer for the next gen
    '''
    #print("Len of polymer at start: %d"% (len(POLY)))
    i = 0
    while i < len(POLY)-1:
        pair = ""
        #print("Pair start: %d" %(i))
        pair += POLY[i]
        pair += POLY[i+1]
        #print("Built pair: %s" % (pair))
        if MAP[pair]:
            #print("Need to insert: %s" % MAP[pair])
            POLY.insert(i+1, MAP[pair])
            i +=1
        else:
            print("No insert found")
        i += 1

def count_poly():
    '''
    Count each item in poly
    '''
    for atom in POLY:
        if atom in COUNTS.keys():
            COUNTS[atom] += 1
        else:
            COUNTS[atom] = 1

LINES = IF.readlines()

for line in LINES:
    line = line.rstrip("\r\n")
    if line == "":
        MODE = 1
        continue
    if MODE == 0:
        for cell in line:
            POLY.append(cell)
    else:
        #(key, add) = re.split(" -> ", line)
        #value = key[0] + add + key[1]
        (key, value) = re.split(" -> ", line)
        MAP[key] = value

print("Original POLY: %s" %  (POLY))

print("Translation Map")
print(MAP)

GEN = 0
while GEN < MAX_GEN:
    #print("Process gen")
    process_gen()
    GEN += 1

#print("After Poly: %s" % (POLY))
print("Len of processed poly: %d" % (len(POLY)))

count_poly()

print("Atom counts:")
#print(COUNTS)
for key, value in COUNTS.items():
    print( "Atom: %s Count: %d" %(key, value))

VALUES = list(COUNTS.values())
print("values: ", VALUES)
MAX = max(COUNTS.values())
MIN = min(COUNTS.values())

print("Max %d\tMin: %d"%(MAX,MIN))
print("Answer: %d"%(MAX-MIN))
