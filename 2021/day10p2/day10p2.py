#!/usr/bin/python3
import re
import numpy as np

IF = open("../day10.data")
#IF = open("../day10.example")
#IF = open("../day10.shortexample")
pushers = { "<", "{", "[", "(" }
poppers = { ">", "}", "]", ")" }

syntax = { 
        "<": ">", 
        "{": "}", 
        "[": "]", 
        "(": ")", 
        }

closingpoints = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
        }

scores = []

for line in IF:
    stack = []
    line = line.rstrip("\r\n")
    #print("Syntax line: %s" % ( line ) )
    i = 0
    corrupted = False
    while i < len(line) and not corrupted:
        part = line[i] 
        #print( "Part: %s" % ( part ) )
        if part in syntax.keys():
            stack.append( part )
        else:
            test = stack.pop()
            #print( "part: %s test %s" % ( part, test ) )
            if test == "[" and part != "]":
#                print( "Expected %s, but found %s instead. Popped: %s" % ("]", part, test) )
                stack.append( test )
                stack.append( part)
                corrupted = True
            elif test == "(" and part != ")":
#                print( "Expected %s, but found %s instead. Popped: %s" % (")", part, test) )
                stack.append( test ) 
                stack.append( part ) 
                corrupted = True
            elif test == "{" and part != "}":
#                print( "Expected %s, but found %s instead. Popped: %s" % ("}", part, test) )
                stack.append( test ) 
                stack.append( part ) 
                corrupted = True
            elif test == "<" and part != ">":
#                print( "Expected %s, but found %s instead. Popped: %s" % (">", part, test) )
                stack.append( test ) 
                stack.append( part ) 
                corrupted = True
            #else:
            #    print( "Found a match at %d ' %s %s '" % ( i, test, part) )
        #print( "Stack contents: " , stack ) 
        i += 1

    answer = 0

    if len(stack) > 0 and not corrupted:
        #print("Remaining stack length: %d" % (len(stack) ) )
        #print("Remaining stack: " , stack )
        i = len(stack) - 1
        while i >= 0:
            part = stack[i]
            i -= 1
            #print( "Need to close: %s" % ( part ) )
            #print("Value: %d" % (closingpoints[part] ) )
            answer *= 5
            if part == "(":
                answer += 1
                #print("Temp Answer = %d" % ( answer ) )
            if part == "[":
                answer += 2
                #print("Temp Answer = %d" % ( answer ) )
            if part == "{":
                answer += 3
                #print("Temp Answer = %d" % ( answer ) )
            if part == "<":
                answer += 4
                #print("Temp Answer = %d" % ( answer ) )
            #print("Partial Answer = %d" % ( answer ) )
        print("Answer = %d" % ( answer ) )
        scores.append( answer )

scores.sort()
print("Score count: %d" % ( len(scores) ) )
midpoint = len(scores)/2
print( "Midpoint: %d" % ( midpoint) ) 
print( "scores: " , scores ) 
print( "Middle score: %d" % ( scores[int(midpoint)] ) )
