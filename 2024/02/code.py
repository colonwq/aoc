#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import argparse
import sys

def p1(input=None, debug=False):
    if debug:
        print("Part 1")
    answer1 = 0
    incline = 0
    valid = True
    lines = []
    if input:
        lines = input.read().splitlines()
        input.seek(0)
        for line in lines:
            valid = True
            incline = 0
            if debug:
              print("Line: %s" %(line) )
            steps = line.split(" ")
            #if debug:
            #  print("steps: %s" %(steps) )
            first = int(steps.pop(0))
            for second in steps:
              if not valid:
                  if debug:
                    print(f"The line is invalid")
                  break
              second = int(second)
              diff = second - first
              if incline == 0:
                  if diff < 0:
                      incline = -1
                  elif diff > 0:
                      incline = 1
                  if debug:
                    print(f"Incline: {incline}")
              if debug:
                print(f"First: {first} Second: {second} Diff: {diff} Incline: {incline}")
              if abs(diff) > 0 and abs(diff) < 4:
                  if incline > 0 and diff > 0:
                      valid = True
                  elif incline < 0 and diff < 0:
                      valid = True
                  else:
                      if debug:
                        print(f"B Incline/diff missmatch Inc: {incline} Diff: {diff}")
                      valid = False
              else:
                if debug:
                    print(f"Differnece exceeded {diff}")
                valid = False

              first = second
            if valid:
                answer1 += 1
                if debug:
                  print("Valid: %s" %(line) )
            else:
                if debug:
                  print("Invalid: %s" %(line) )

    print("Wrong answers: [0]")
    print(f"Answer 1: {answer1}")

def p2(input=None, debug=False):
    if debug:
        print("Part 2")
    answer2 = 0
    incline = 0
    valid = 0
    lines = []
    if input:
        lines = input.read().splitlines()
        input.seek(0)
        for line in lines:
            valid = 0
            incline = 0
            if debug:
              print("Line: %s" %(line) )
            steps = line.split(" ")
            #if debug:
            #  print("steps: %s" %(steps) )
            first = int(steps.pop(0))
            for second in steps:
              if valid > 1:
                  if debug:
                    print(f"The line is invalid")
                  break
              second = int(second)
              diff = second - first
              if incline == 0:
                  if diff < 0:
                      incline = -1
                  elif diff > 0:
                      incline = 1
                  if debug:
                    print(f"Incline: {incline}")
              if debug:
                print(f"First: {first} Second: {second} Diff: {diff} Incline: {incline}")
              if abs(diff) > 0 and abs(diff) < 4:
                  if incline > 0 and diff > 0:
                      valid += 0
                  elif incline < 0 and diff < 0:
                      valid += 0
                  else:
                      if debug:
                        print(f"B Incline/diff missmatch Inc: {incline} Diff: {diff}")
                      valid += 1
              else:
                if debug:
                    print(f"Differnece exceeded {diff}")
                valid += 1

              first = second
            if valid < 2:
                answer2 += 1
                if debug:
                  print("Valid: %s" %(line) )
            else:
                if debug:
                  print("Invalid: %s" %(line) )

    print("Wrong answers: [0]")
    print(f"Answer 2: {answer2}")

def main():
    """Script entry point"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", nargs='?', default="../data/02.txt", help="Input data file")
    parser.add_argument("--debug", "-d", default=False, help="Enable debuging", action="store_true")
    parser.add_argument("-p1", help="Do part 1", action="store_true")
    parser.add_argument("-p2", help="Do part 2", action="store_true")
    args = parser.parse_args()

    if args.file:
        if args.debug:
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

    file_input.close()

if __name__ == "__main__":
    main()
