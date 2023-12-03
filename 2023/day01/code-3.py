#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
import regex as re

replacements = {
"zerone": "zeroone",
"oneight": "oneeight",
"twone": "twoone",
"sevenine": "sevennine",
"eightwo": "eighttwo",
"eighthree": "eightthree",
"nineight": "nineeight"
}

number_table = {
  "zero":  "0",
  "one":   "1",
  "two":   "2",
  "three": "3",
  "four":  "4",
  "five":  "5",
  "six":   "6",
  "seven": "7",
  "eight": "8",
  "nine":  "9"
  }

def process_line(line = "1Here be dragons 7"):
  retval = ""

  for replacement in replacements.keys():
    line = line.replace(replacement, replacements[replacement])

  for number in number_table:
    line = line.replace(number, number_table[number])

  matches = re.findall("\d+",line)
  first = matches[0][0]
  last = matches[-1][-1]

  answer = int(first+last)
  return answer

def main():
    """Script entry point"""
    answer = 0
    numbers = []

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
        answer += process_line(line)

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
