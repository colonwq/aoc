#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def build_set(zone):
    '''this will take a start-stop range and build a set'''
    myset = set()
    start, stop = zone.split("-")
    start = int(start)
    stop = int(stop)
    while start <= stop:
        myset.add(start)
        start+=1
    #print("MySet: ", myset)
    return myset


def compare_zone(zones):
    '''this will take the zone list and comapre complete for overlap'''
    zonea, zoneb = zones.split(",")
    #print("ZoneA: %s Zone B: %s" % ( zonea, zoneb) )
    zonea = build_set(zonea)
    zoneb = build_set(zoneb)
    return not zonea.isdisjoint(zoneb)
    #if not zonea.isdisjoint(zoneb):
    #    return True
    #else:
    #    return False

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    #file_input = open(sys.argv[1], "r")

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
        if compare_zone(line):
            answer  += 1

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
