#!/usr/bin/python3
'''
Solution for Day01 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def main():
    """Script entry point"""
    #print("Hello World")
    goal = 2020
    values = []

    file_input = open(sys.argv[1], "r")

    for line in file_input:
        line = line.strip("\n")
        #print("Input line: %s" % (line) )
        values.append(int(line))

    #print("values: ", values )

    for test in values:
        possible_answer = goal - test
        #print("Possible answer: %d" % ( possible_answer) )
        try:
            index = values.index(possible_answer)
        except ValueError:
            #print("No solution found")
            pass
        else:
            #print("Found a solution at index %d" % (index) )
            answer = test*possible_answer
            print("Answer: %d\n" % (answer) )
            exit()


if __name__ == "__main__":
    main()
