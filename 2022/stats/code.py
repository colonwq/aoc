#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def main():
    """Script entry point"""
    print("Hello World")
    answer = 0

    try:
        file_input = open(sys.argv[1], "r")
    except Exception as e:
        print("Error opening file: ", e)
        exit()

    for line in file_input:
        line = line.strip("\n")
        print("Line: %s"% (line) )

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
