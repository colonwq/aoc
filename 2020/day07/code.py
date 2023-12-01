#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
import re

def process_line(line="These bags contain 1 dragon, 2 good bois"):
    retval = 0
    bags = {}

    line = line.replace(" bags contain ",":")
    #print("Interum Line: %s"%(line))
    line = line.replace("bags","bag")
    #print("Interum Line: %s"%(line))
    line = line.replace(".",",")
    #print("Interum Line: %s"%(line))
    line = line.replace(" bag,",":")
    line = line.replace(": ",":")
    #print("Interum Line: %s"%(line))
    line = line.rstrip(":")
    #print("Interum Line: %s"%(line))

    parts = line.split(":")
    # print("Master bag: %s"%(parts[0]))
    master = parts[0]
    parts.pop(0)

    for part in parts:
        #print("Contained bags: %s" %(part))
        if part.find("no other") >= 0:
            bag = "no other"
            count = 0
        else:
            (count, bag) = part.split(" ", 1)
        # print("Count: %s Bag: %s"%(count, bag))
        bags[bag] = count
    return master, bags

def check_for_bag(master_table , my_bag ):
    retval = 0
    #print("Master table: " , master_table)
    for test_bag in master_table:
        possible_bags_dict = master_table[test_bag]
        print("Test Bag: %s Possible bags: " %(test_bag), possible_bags_dict)
        # print("Type: ", type(possible_bags_dict))
        found = possible_bags_dict.get(my_bag, 0)
        #print("Found %s in bag %s" % (found, test_bag))
        #keys = master_table[test_bag].list()
        #print("Keys: ", keys)
        if found:
            print("Found %s in bag %s" % (found, test_bag))
            retval += 1
        else: 
            for poss_key in possible_bags_dict.keys():
                print("Possible key: %s" %( poss_key))
                if poss_key in master_table.keys():
                    test_keys = master_table[poss_key].keys()
                    if my_bag in test_keys:
                        print("Found %s also in %s"% (my_bag, poss_key))
                        retval += 1
                

        
    return retval

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    master_table = {}
    my_bag = "shiny gold"

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
        #print("Original Line: %s" %(line) )
        (master, bags) = process_line(line)
        #print("%s contains " %(master), bags)
        master_table[master] = bags
    answer = check_for_bag(master_table, my_bag)

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
