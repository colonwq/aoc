#!/usr/bin/env python3
'''
Solution for Day06 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def process(answers):
    retval = 0

    #print("Answers: ", answers)

    first_responce = True
    responce = set()

    for answer in answers:
        new_responce = set()
        index = 0
        while index < len(answer):
            #print("Adding: ", answer[index])
            new_responce.add(answer[index])
            index += 1
        if first_responce == True:
            responce = new_responce
            first_responce = False
        else:
            responce = responce.intersection(new_responce)
            #print("Interum intersection: " , responce)
    #print(responces)
    #print("Final intersection: " , responce)
    retval = len(responce)
    #print("Unique answers: %d" % (retval))

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
