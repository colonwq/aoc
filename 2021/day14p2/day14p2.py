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
MAX_GEN = 40
COUNTS = {}
PAIRS = {}

def gen_polypairs( poly ):
    '''
    Take the poly POLY string and generate pairs map and count
    '''
    my_pairs = {}
    i = 0
    while i < len(poly)-1:
        pair = ""
        pair += poly[i]
        pair += poly[i+1]
        if pair in my_pairs.keys():
            my_pairs[pair] += 1
        else:
            my_pairs[pair] = 1
        i += 1
    return my_pairs

def process_gen_2(pair):
    '''
    Grow polymer pairs for the next gen
    '''
    new_pairs = {}
    for poly_key, poly_value in pair.items():
        #print("Poly pair: %s" % (poly_key))

        if poly_key in MAP.keys():
            #print("Poly pair %s maps to %s" % (poly_key, MAP[poly_key]))
            first_pair = poly_key[0] + MAP[poly_key]
            second_pair = MAP[poly_key] + poly_key[1]
            #print("Adding new pairs: %s, %s"%(first_pair, second_pair))
            if first_pair in new_pairs.keys():
                #print("%s already in new_pairs"% (first_pair))
                new_pairs[first_pair] += poly_value
            else:
                new_pairs[first_pair] = poly_value
            if second_pair in new_pairs.keys():
                #print("%s already in new_pairs"% (second_pair))
                new_pairs[second_pair] += poly_value
            else:
                new_pairs[second_pair] = poly_value
        else:
            print("Poly pair %s NOT in map"% ( poly_pair))
    return new_pairs

def count_poly(pairs):
    '''
    Count each item in poly
    '''
    atom_count = {}
    for pair, value in pairs.items():
        print("Looking at pair: %s" % (pair))
        print("First atom: %s"% (str(pair[0])))
        #print("Second atom: %s"% (str(pair[1])))
        if pair[0] in atom_count.keys():
            print("Already found %s %d times"%(pair[0], atom_count[pair[0]]))
            atom_count[pair[0]] += value
        else:
            atom_count[pair[0]] = value
    print("Adding 1 for %s" % (pair[1]))
    atom_count[pair[1]] += 1

    return atom_count

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
PAIRS = gen_polypairs(POLY)
print("Original poly pairs: " , PAIRS )
print("Translation Map")
print(MAP)

GEN = 0
while GEN < MAX_GEN:
    #print("Process gen")
    PAIRS = process_gen_2(PAIRS)
    GEN += 1

print("Poly pair map\n", PAIRS)
COUNTS = count_poly(PAIRS)

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
