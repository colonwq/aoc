#!/usr/bin/python3
'''
Solution for Day02 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def test_password(min_char, max_char, req_char, password):
    #print("min: %d max: %d req:%s password: %s" %(min_char, max_char, req_char, password) )
    found = 0
    for test_char in password:
        if test_char == req_char:
            #print("test_char matches req_char: %s -> %s" % (test_char, req_char) )
            found+=1
    #print("Found count: %d" % (found) )
    if found >= min_char and found <= max_char:
        #print("Valid password: %s" % (password) )
        return True
    else:
        return False

def main():
    """Script entry point"""
    #print("Hello World")
    good_passwords = 0

    file_input = open(sys.argv[1], "r")

    for line in file_input:
        line = line.strip("\n")
        #print("Input line: %s" % (line) )
        #parts = line.split(": ")
        #print("key: %s\tpassword:%s" %(parts[0],parts[1]))
        req, password = line.split(": ")
        #print("key: %s\tpassword:%s" %( req, password))
        minmax, req_char = req.split(" ")
        #print("minmax: %s req:%s password: %s" %(minmax, req_char, password) )
        min_char, max_char = minmax.split("-")
        #print("min:%s max: %s req:%s password: %s" %(min_char, max_char, req_char, password) )
        if test_password(int(min_char), int(max_char), req_char, password):
            good_passwords+=1

    print("Good Passwords: ", good_passwords )

if __name__ == "__main__":
    main()
