#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
import numpy

calories = []

def main():
    """Script entry point"""
    print("Hello World")
    print("File Argument: %s" % (sys.argv[1]) )

    input = open(sys.argv[1], "r") 

    cal = 0
    for line in input:
        line2 = line.strip("\n")
        if len(line2) > 0:
            #print("Input %s" % line2 )
            #print("Number: %d" % (int(line2) ) )
            cal += int(line2)
        else:
            #print("Total cals: %d"% (cal) )
            calories.append(cal)
            cal = 0
            #print("New Elf")
    calories.append(cal)
    #print("Total cals: %d"% (cal) )

    #print("Calories: ", calories )
    #max_ind = numpy.argmax(calories)
    #print("Max index: %d (%d)" % ( max_ind+1, calories[max_ind] ) )
    #print("Max value: %d" % (max(calories) ) )

    i = 0;
    while i < len(calories):
        print("%d <- %d" % ( calories[i] , i ) )
        i+=1

if __name__ == "__main__":
    main()
