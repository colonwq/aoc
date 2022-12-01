#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
import numpy

def main():
    """Script entry point"""
    calories = []
    top_3_cal = 0

    #open the data file
    input_file = open(sys.argv[1], "r")

    cal = 0
    for line in input_file:
        #each line is a calorie amount
        line2 = line.strip("\n")
        if len(line2) > 0:
            cal += int(line2)
        else:
            #a blank line is a new elf
            #store the current values and restart
            calories.append(cal)
            cal = 0
    #last calorie of the last elf
    #store it
    calories.append(cal)

    #find the max index 3 times
    #add this calorie to top_3_cal
    #then delete it
    max_ind = numpy.argmax(calories)
    top_3_cal += calories[max_ind]
    calories.pop(max_ind)

    max_ind = numpy.argmax(calories)
    top_3_cal += calories[max_ind]
    calories.pop(max_ind)

    max_ind = numpy.argmax(calories)
    top_3_cal += calories[max_ind]
    calories.pop(max_ind)

    print("Top 3 sum: %d" % (top_3_cal) )

if __name__ == "__main__":
    main()
