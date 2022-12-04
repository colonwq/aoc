#!/usr/bin/python3
'''
  Day 13 part 1
'''
import re
import numpy as np

IF = open("../day13.data")
#IF = open("../day13.demo")
MODE = 0
COUNT = 0
MAXX = 0
MAXY = 0

PAPER = []
POINTS = []
COMMANDS = []
LINES = IF.readlines()
LINES = [line.rstrip() for line in LINES]

def print_paper(my_paper):
    '''
    Print the paper grid
    '''
    for row in my_paper:
        print(row)

def count_dots():
    '''
    Count the dots on the paper
    '''
    count = 0
    for row in PAPER:
        for cell in row:
            if cell > 0:
                count += 1
    return count

def fold_up( row ):
    '''
    Fold the paper up along a given row
    '''
    print("Need to fold along row %d" % (row))
    row_count = len(PAPER)
    bottom_count = row_count - row

    #print("Bottom of the paper size: %d" % (bottom_count))
    #print("Top of the paper size: %d" % (row))

    #copy the top into a new paper
    new_paper = []
    i = 0
    while i < row:
        new_paper.append(list(PAPER[i]))
        i += 1
    #print("New paper size: %d" % (len(new_paper)))
    #print_paper(new_paper)

    #print("Lines to fold up")
    i = row-1
    for j in PAPER[row+1:]:
        #print("Bottom: ",j)
        #print("Top:    ", new_paper[i])
        x = 0
        while x < len(j):
            new_paper[i][x] += j[x]
            x += 1
        #we may roll off the top
        i -= 1

    #print_paper(new_paper)
    return new_paper

def fold_left( column ):
    '''
    Fold the paper left along a given row
    '''
    print("Need to fold along column %d" % (column))
    column_count = len(PAPER[0])
    right_count = column_count - column

    #print("Right of the paper size: %d" % (right_count))
    #print("Left of the paper size: %d" % (column))
    #copy the left into a new paper
    new_paper = []
    for oldrow in PAPER:
        new_paper.append(list(oldrow[0:column]))
        #print("New row:   ", new_paper[-1] )
        #print("Right row: ", oldrow[column+1:])
        j = column-1
        for cell in oldrow[column+1:]:
            new_paper[-1][j] += cell
            #this may underflow a row
            j -= 1

    #print_paper( new_paper )
    return new_paper

for line in LINES:
    #line = line.rstrip("\r\n")
    if line == "":
        MODE = 1
        continue
    if MODE == 0:
        (x, y) = re.split(",", line)
        point = {}
        point["x"] = int(x)
        point["y"] = int(y)

        POINTS.append(point)
        #print("X: %d, Y: %d"% (POINTS[-1]["x"], POINTS[-1]["y"]))
        MAXX = max(MAXX, POINTS[-1]["x"])
        MAXY = max(MAXY, POINTS[-1]["y"])
    else:
        #print("Command: %s" % (line))
        line = re.sub("fold along ", "", line)
        #print("Command: %s" % (line))
        command = {}
        (direction, target) = re.split("=", line)
        command['direction'] = direction
        command['target'] = int(target)
        COMMANDS.append(command)

print("Max X: %d" % (MAXX))
print("Max Y: %d" % (MAXY))

Y = 0
while Y <= MAXY:
    PAPER.append(np.zeros(MAXX+1))
    Y += 1

for point in POINTS:
    PAPER[point["y"]][point["x"]] = 1

#print_paper(PAPER)

print("Number of commands: %d" % len(COMMANDS))

COMMAND = COMMANDS.pop(0)

print("Command: ", COMMAND )

if COMMAND['direction'] == "y":
    #print("Fold up")
    PAPER = fold_up(COMMAND['target'])
elif COMMAND['direction'] == 'x':
    print("Fold left")
    #PAPER = fold_left(COMMAND['target'])
    PAPER = fold_left(COMMAND['target'])

#for COMMAND in COMMANDS[:0]:
#    print("Command: ", COMMAND )
#
#    if COMMAND['direction'] == "y":
#        #print("Fold up")
#        PAPER = fold_up(COMMAND['target'])
#    elif COMMAND['direction'] == 'x':
#        print("Fold left")
#        #PAPER = fold_left(COMMAND['target'])
#        PAPER = fold_left(COMMAND['target'])

COUNT = count_dots()

print("Total dots seen: %d" % (COUNT))
