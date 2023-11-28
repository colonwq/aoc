#!/usr/bin/env python3
'''
Solution for Day05 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
import numpy as np


def process(line="FBFBBFFRLR"):
    retval = 0
    rows = np.array(range(0,127))
    cols = np.array(range(0,8))
    #print("Processing line: %s Length: %d" % ( line, line.__len__() ))

    count = 0
    window = 128
    while count <= 7:
        #print("Count: %d Window: %d" %(count,window))
        window /= 2
        if line[count] == "F":
            rows = rows[:int(window)]
        if line[count] == "B":
            rows = rows[int(window):]
        count += 1 

    #print("Final row: %d" %( rows[0]))
        
    window = 8
    count -= 1
    #print("Possible seats: ", cols )
    while count < line.__len__():
        #print("Count: %d Window: %d" %(count,window))
        window /= 2
        if line[count] == "R":
            #print("Found R")
            cols = cols[int(window):]
        if line[count] == "L":
            #print("Found L")
            cols = cols[:int(window)]
        count += 1 
        #print("Possible seats: ", cols )

    #print("Final col: %d" %( cols[0]))

    #retval = rows[0] * 8 + cols[0]

    return rows[0], cols[0]

def findseat(airplane):
    my_row = my_col = retval = 0

    for row in range(1,126):
        for col in range(1,6):
            #print( "Looking at [%d][%d]= (%d)" % ( row, col, airplane[row][col]))
#            if row == 78 and col == 1:
#                print("Current: %d"%(airplane[row][col]))
#                print("left:    %d"%(airplane[row-1][col]))
#                print("right:   %d"%(airplane[row+1][col]))
#                print("up:      %d"%(airplane[row][col-1]))
#                print("down:    %d"%(airplane[row][col+1]))
            if airplane[row][col] == 0 and airplane[row-1][col] == 1 and airplane[row+1][col] == 1 and airplane[row][col-1] == 1 and airplane[row][col+1] == 1:
                my_row = row
                my_col = col
                print("Found my seat at row: %d col %d" % (my_row, my_col))

    retval = my_row * 8 + my_col
    return retval

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    answers = []
    airplane = []
    
    row = 0
    while row < 127:
        airplane.append([0]*8)
        row += 1

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    lines = file_input.read().splitlines()
    for line in lines:
        #print("Line: %s" %(line) )
        (row, col) = process(line)
        #print( "Row: %d Col: %d" % (row, col))
        airplane[row][col] = 1

    answer = findseat(airplane)
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
