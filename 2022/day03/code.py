#!/usr/bin/python3
'''
Solution for Day03 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def find_missing(sack):
    '''this function finds the item missing from the second half of the sack'''
    missing = []
    #print("sack: %s" %(sack))
    #print("Sack len: %d" % (len(sack) ) )
    sack_len = int(len(sack)/2)
    #print("Sack half len: %d" % (sack_len ) )
    #print("Sack len type: ", type(sack_len) )
    first = sack[:sack_len]
    second = sack[sack_len:]
    #print("First: %s" %( first) )
    #print("Second: %s"%(second))
    for item in first:
        if item in second:
            #print("Missing %s" % (item) )
            missing.append(item)

    #get unique items
    missing = list(set(missing))
    return missing[0]

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    rucksack = []
    missing = []
#    print("Ascii value of a: %d" %(ord("a")))
#    print("Ascii value of z: %d" %(ord("z")))
#    print("Ascii value of A: %d" %(ord("A")))
#    print("Ascii value of Z: %d" %(ord("Z")))

    try:
        file_input = open(sys.argv[1], "r")
    except Exception as e_exception:
        print("Error opening file: ", e_exception)
        sys.exit()

    for line in file_input:
        line = line.strip("\n")
        #print("Line: %s"% (line) )
        rucksack.append(line)

    for sack in rucksack:
        missing.append(find_missing(sack))

    print("Missing Items: ", missing )
    for item in missing:
        item_ord = ord(item)
#        print("Pre-Missing item: %s(%d)" %( item, item_ord) )
        if item_ord >=97 and item_ord <= 122:
#            print("Lower case %d"%(item_ord))
            item_ord-=96
        elif item_ord >= 65 and item_ord <= 90:
#            print("Before Upper case %d"%(item_ord))
            item_ord = item_ord-38
#            print("--------AFTER Upper case %d"%(item_ord))
#        print("Missing item: %s(%d)" %( item, item_ord) )
        answer += item_ord

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
