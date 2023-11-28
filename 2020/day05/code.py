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
    print("Processing line: %s Length: %d" % ( line, line.__len__() ))

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

    print("Final row: %d" %( rows[0]))
        
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

    print("Final col: %d" %( cols[0]))

    retval = rows[0] * 8 + cols[0]

    return retval

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    answers = []

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
        print("Line: %s" %(line) )
        answers.append( process(line) )

    answer = max(answers)
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
