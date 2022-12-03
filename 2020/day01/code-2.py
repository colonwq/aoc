#!/usr/bin/python3
'''
Solution for Day01 part 2
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def find_pair( values, goal, first):
    """This will take the first value
    and iterate across the values to find a possible answer
    """

    for second in values:
        possible_answer = goal - first - second
        #print("Possible answer: %d" % ( possible_answer) )

        try:
            index = values.index(possible_answer)
        except ValueError:
            #print("No solution found")
            pass
        else:
            #print("Found a solution at index %d" % (index) )
            answer = first*second*possible_answer
            print("Answer: %d\n" % (answer) )
            exit()

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
        find_pair(values, goal, test)
        #possible_answer = goal - test

        #print("Possible answer: %d" % ( possible_answer) )


if __name__ == "__main__":
    main()
