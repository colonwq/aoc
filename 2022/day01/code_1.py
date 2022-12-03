#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys


def main():
    """Script entry point"""
    max_cal = 0
    elf = 0
    #print("File Argument: %s" % (sys.argv[1]) )

    file_input = open(sys.argv[1], "r")

    cal = 0
    end_of_elf = 0
    for line in file_input:
        line2 = line.strip("\n")
        if len(line2) > 0:
            cal += int(line2)
        else:
            end_of_elf += 1
            if cal > max_cal:
                max_cal = cal
                elf = end_of_elf
            cal = 0
            #print("New Elf")
    #print("Last elf")
    end_of_elf += 1
    if cal > max_cal:
        max_cal = cal
        elf = end_of_elf

    print("Max calorie: %d" %(max_cal) )
    print("Elf: %d" % (elf) )


if __name__ == "__main__":
    main()
