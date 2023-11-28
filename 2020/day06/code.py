#!/usr/bin/env python3
'''
Solution for Day06 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def process(answers):
    retval = 0

    print("Answers: ", answers)
    responces = {}

    for answer in answers:
        index = 0
        while index < len(answer):
            responces[answer[index]] = 1
            index += 1
    #print(responces)
    retval = len(responces)
    print("Unique answers: %d" % (retval))

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
        #print("Line: %s" %(line) )
        if len(line) == 0:
            answer += process(answers)
            #print("Line: %s" %(line) )
            answers = []
        else:
            answers.append(line)
    answer += process(answers)

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
