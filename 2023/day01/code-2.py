#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''
#corret 54985
import sys

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
#  for spot in line:
#    #I could have done it with re
#    if spot.isdigit():
#      retval += spot
  i = 0
  while i < len(line):
    if line[i].isdigit():
       retval += line[i]
    else: 
       for test_num in number_table.keys():
          if line.find(test_num, i) == i:
             #print("Found %s at pos %d in %s"%(test_num, i, line))
             retval += number_table[test_num]
             #i+=(len(test_num)-1)
    i+=1
    #print("next substring: %s" % (line[i:]))

  print("Returning: %s"%(retval))
  return retval

def find_numbers( number = "123"):
  retval = "0"

  if len(number) > 0 :
    first_digit = number[0]
    last_digit = number[-1]
    #print("First: %s Last: %s"%(first_digit,last_digit))
    retval = first_digit + last_digit
  return int(retval)

def main():
    """Script entry point"""
    #print("Hello World")
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
        print("Line: %s" %(line) )
        numbers.append(process_line(line))

    #print("All numbers found: " , numbers)
    for number in numbers:
      answer += find_numbers(number)
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
