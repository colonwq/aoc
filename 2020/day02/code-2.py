#!/usr/bin/python3
'''
Solution for Day02 part 2
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def test_password(first_pos, second_pos, req_char, password):
    #print("first pos: %d second pos: %d req:%s password: %s" %(first_pos, second_pos, req_char, password) )
    found = 0
    return (password[first_pos-1] == req_char) != (password[second_pos-1] == req_char)

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
        #test_password(int(min_char), int(max_char), req_char, password)
        if test_password(int(min_char), int(max_char), req_char, password):
            #print("Good: %s" %  ( line ) )
            good_passwords+=1

    print("Good Passwords: ", good_passwords )

if __name__ == "__main__":
    main()
