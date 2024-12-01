#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import argparse
import sys

def p1(input=None, debug=False):
    print("Part 1")
    lines = []
    if input:
        lines = input.read().splitlines()
        input.seek(0)
        for line in lines:
            if debug:
              print("Line: %s" %(line) )

def p2(input=None, debug=False):
    print("Part 2")
    lines = []
    if input:
        lines = input.read().splitlines()
        for line in lines:
            if debug:
              print("Line: %s" %(line) )

def main():
    """Script entry point"""
    print("Hello World")

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", nargs='?', default="../data/00.txt", help="Input data file")
    parser.add_argument("--debug", "-d", help="Enable debuging", action="store_true")
    parser.add_argument("-p1", help="Do part 1", action="store_true")
    parser.add_argument("-1", help="Do part 1", action="store_true")
    parser.add_argument("-p2", help="Do part 2", action="store_true")
    args = parser.parse_args()

    answer = 0

    print(f"Parser: {args}")

    if args.file:
        print(f"Input file: {args.file}")
        if args.p1:
            print(f"Do part 1")
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

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
