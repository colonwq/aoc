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

error_count = {
        ")": 0,
        "]": 0,
        "}": 0,
        ">": 0,
        }
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
                print( "Expected %s, but found %s instead. Popped: %s" % ("]", part, test) )
                stack.append( test )
                stack.append( part)
                error_count[ part ] += 1
                corrupted = True
            elif test == "(" and part != ")":
                print( "Expected %s, but found %s instead. Popped: %s" % (")", part, test) )
                stack.append( test ) 
                stack.append( part ) 
                error_count[ part ] += 1
                corrupted = True
            elif test == "{" and part != "}":
                print( "Expected %s, but found %s instead. Popped: %s" % ("}", part, test) )
                stack.append( test ) 
                stack.append( part ) 
                error_count[ part ] += 1
                corrupted = True
            elif test == "<" and part != ">":
                print( "Expected %s, but found %s instead. Popped: %s" % (">", part, test) )
                stack.append( test ) 
                stack.append( part ) 
                error_count[ part ] += 1
                corrupted = True
            #else:
            #    print( "Found a match at %d ' %s %s '" % ( i, test, part) )
        #print( "Stack contents: " , stack ) 
        i += 1
#    print("Remaining stack length: %d" % (len(stack) ) )
#    print("Remaining stack: " , stack )

print("Missing counts:" , error_count)
answer = error_count[ ")" ] * 3
answer += error_count[ "]" ] * 57
answer += error_count[ "}" ] * 1197
answer += error_count[ ">" ] * 25137
#answer = 0
#print("Answer = %d" % ( (count_paren*3 + count_square*57 + count_curly*1197 + count_angle*25137) ) )
print("Answer = %d" % ( answer ) )
