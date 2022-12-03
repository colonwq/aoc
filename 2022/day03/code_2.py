#!/usr/bin/python3
'''
Solution for Day03 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def find_missing(sack):
    '''This will find the element in the first half that is missing from thesecond'''
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
def find_same(search):
    '''this will find the common element in the 3 search sacks'''
    #print("Searching sacks: " , search)
    set_a = set(search[0])
    set_b = set(search[1])
    set_c = set(search[2])
    #print(set_a.union(set_b.union(set_c)))
    #print(list(set_a.intersection(set_b,set_c)))
    return list(set_a.intersection(set_b,set_c))


def main():
    """Script entry point"""
    #print("Hello World")
    size=3
    answer = 0
    rucksack = []
    same = []

    try:
        file_input = open(sys.argv[1], "r")
    except Exception as e_exception:
        print("Error opening file: ", e_exception)
        sys.exit()

    for line in file_input:
        line = line.strip("\n")
        #print("Line: %s"% (line) )
        rucksack.append(line)

    #print("Number of sacks: %d" % (len(rucksack)))
    segments = int(len(rucksack)/size)
    #print("Number of segments: %d" % (segments))

    count = 0
    while count < segments:
        #print("Looking at segment:%d"%(count))
        #print("Looking at offst %d:%d" %(count*size,(count*size)+3))
        same += find_same(rucksack[count*size:(count*size)+3])
        count+=1

    for item in same:
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
