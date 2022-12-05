#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
from collections import deque

def build_stack(intake):
    '''building the initial stack of boxes'''
    print("Building the stacks")
    num_stacks = int(len(intake[0])/3)
    stack = {}

    #print("Stacks: ", stack)
    #for line in intake:
    #    print("line: ", line)

    for line in intake:
        if not ( line.startswith(" 1")):
            #print("Line (str) : " , (line))
            line = list(line)
            #print("Line (list): " , (line))
            for loc in range(1, len(line), 4):
                if str(line[loc]).isalpha():
                    stack_loc = int(loc/4)+1
                    stack_loc_str = str(stack_loc)
                    #print("Found a crate (%s) at loc(%d) stack: %s"%(line[loc],loc, stack_loc_str))
                    if stack_loc_str not in stack:
                        #print("Creating a stack list at %s" %(stack_loc_str))
                        stack[stack_loc_str] = deque([])
                    #stack[stack_loc_str].append(line[loc])
                    stack[stack_loc_str].insert(0,line[loc])
        else:
            #print("Returning stack\n", stack)
            return stack

def move_stacks(stacks, intake):
    '''This will move boxes between stacks as 
    per the line given. '''
    print("Moving stacks")
    for line in intake:
        if not line.startswith("move"):
            next
        else:
            #print("Command: %s"%(line))
            parts = line.split(" ")
            parts[1] = int(parts[1])
            amount = parts[1]
            source = parts[3]
            dest   = parts[5]
            #print("Amount = %d From: %s To: %s" % (parts[1], parts[3], parts[5]) )
            #print("Amount = %d From: %s To: %s" % (amount, source, dest))
            count = 0
            while count < amount:
                crate = stacks[source].pop()
                stacks[dest].append(crate)
                #stacks[dest].push( stacks[source].pop() )
                #print("Stacks: " , stacks )
                count += 1

    #keys = stacks.keys()
    keys = []
    for key in stacks.keys():
        keys.append(int(key))
    #print("Unsorted Stack keys: ", keys)
    keys.sort()
    #print("Sorted Stack keys: ", keys)
    answer = ""
    for key in keys:
        #print( stacks[str(key)].pop() )
        answer = answer + stacks[str(key)].pop()
    #print("Answer: %s"% (answer) )
    return answer

def main():
    """Script entry point"""
    print("Hello World")
    answer = 0
    #file_input = open(sys.argv[1], "r")
    stacks = []
    intake = []

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    for line in file_input:
        line = line.strip("\n")
        #print("Line: %s"% (line) )
        intake.append(line)

    #print("Intake: ", intake)
    stacks = build_stack(intake)
    #print("Returned stacks\n" , stacks)
    answer = move_stacks(stacks, intake)

    print("Answer " , answer )

if __name__ == "__main__":
    main()
