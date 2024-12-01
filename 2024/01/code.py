#!/usr/bin/env python3
'''
Solution for Day01 part 1 and 2
This is a generic file for all days.
Copy this directory to the new day and part
'''

import argparse
import sys

def p1(input=None, debug=False):
    #print("Part 1")
    answer1 = 0
    lines = []
    list1 = []
    list2 = []
    if input:
        lines = input.read().splitlines()
        input.seek(0)
        for line in lines:
            if debug:
              print("Line: %s" %(line) )
            a, b = line.split("   ")
            list1.append(int(a))
            list2.append(int(b))
        list1.sort()
        list2.sort()
        if debug:
            print(f"{list1}")
            print(f"{list2}")
        i = 0
        while i < len(list1):
            a = list1[i]
            b = list2[i]
            diff = a - b
            if debug:
                print(f"A: {a} B: {b} Diff: {diff}")
            answer1 += abs(diff)
            i += 1
    print(f"Answer1: {answer1}")
    return answer1

def p2(input=None, debug=False):
    #print("Part 2")
    answer2 = 0
    list1 = []
    list2 = []
    lines = []
    if input:
        lines = input.read().splitlines()
        for line in lines:
            if debug:
              print("Line: %s" %(line) )
            a, b = line.split("   ")
            list1.append(int(a))
            list2.append(int(b))
        i = 0
        while i < len(list1):
            part = list1[i] * list2.count(list1[i])
            if debug:
              print(f"Part: {part}")
            answer2 += part
            i += 1

    print(f"Answer 2: {answer2}")
    return answer2

def main():
    """Script entry point"""
    #print("Hello World")

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", nargs='?', default="../data/00.txt", help="Input data file")
    parser.add_argument("--debug", "-d", help="Enable debuging", action="store_true")
    parser.add_argument("-p1", help="Do part 1", action="store_true")
    parser.add_argument("-p2", help="Do part 2", action="store_true")
    args = parser.parse_args()

    #print(f"Parser: {args}")

    if args.file:
        print(f"Input file: {args.file}")
        try:
            file_input = open(args.file, "r")
        except IndexError as i_exception:
            print("No file given: ", i_exception)
            sys.exit()
        except FileNotFoundError as f_exception:
            print("File not found: ", f_exception)
            sys.exit()

    if args.p1:
        p1(input=file_input, debug=args.debug)
    if args.p2:
        p2(input=file_input, debug=args.debug)
    if not args.p1 and not args.p2:
        p1(input=file_input, debug=args.debug)
        p2(input=file_input, debug=args.debug)

if __name__ == "__main__":
    main()
