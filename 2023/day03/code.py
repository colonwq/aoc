#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def build_number(lines = [], j = 0, i = 0):
  found_number = 0
  built_number = ""
  #print("Building a number starting at [%d][%d]" %( j, i) )
  ileft = i-1
  row_list = list( lines[j] )
  while ileft >= 0 and row_list[ileft].isdigit():
    built_number = row_list[ileft] + built_number
    row_list[ileft] = "."
    ileft -= 1
  iright = i
  while iright < len(lines[j]) and row_list[iright].isdigit():
    built_number = built_number + row_list[iright]
    row_list[iright] = "."
    iright += 1
  lines[j] = "".join(row_list)
  #print("Built Number: %s" % (built_number) )
  if len(built_number) > 0:
    found_number = int(built_number)
  return found_number

def find_numbers(lines = [], j = 0, i = 0):
  number_sum =  0

  #search row up j-1 from i-1 to i+1
  if j > 0:
    jup = j-1
    for iup in range( max(0,i-1), min(i+2, len(lines[jup]) ) ):
      if lines[jup][iup].isdigit():
        #print("Found a digit up in [%d][%d](%s)"%(jup,iup,lines[jup][iup]))
        number_sum += build_number(lines,jup,iup)
      #search row down j+1 from i-1 to i+1
  if j < len(lines)-1:
    jdown = j+1
    for idown in range( max(0,i-1), min(i+2, len(lines[jdown]) ) ):
      if lines[jdown][idown].isdigit():
        #print("Found a digit down in [%d][%d](%s)"%(jdown,idown,lines[jdown][idown]))
        number_sum += build_number(lines,jdown,idown)
  #search i-1
  if i > 0:
    ileft = i-1
    #print("Left: [%d][%d](%s)" % (j, i, lines[j][ileft]) )
    if lines[j][ileft].isdigit():
      #print("Found a digit left in [%d][%d](%s)" % ( j, i, lines[j][ileft] ) )
      number_sum += build_number(lines,j,ileft)
  #search i+1
  if i < len(lines[j])-1:
    iright = i+1
    #print("Right: [%d][%d](%s)" % (j, i, lines[j][iright]) )
    if lines[j][iright].isdigit():
      #print("Found a digit left in [%d][%d](%s)" % ( j, i, lines[j][iright] ) )
      number_sum += build_number(lines,j,iright)

  #print("Number sum: %d" %(number_sum) )
  return number_sum
  

def process_lines( lines = [] ):
  retval = j = i = 0
  retvals = []
  while j < len(lines):
    while i < len(lines[0]):
      if not lines[j][i].isdigit() and lines[j][i] != ".":
        #cprint("Found a part at [%d %d] %s" %(j,i,lines[j][i]))
        retval += find_numbers(lines, j, i)
        #print("Sum of adjacent part numbers: %d" %(retval))
      i += 1
    j += 1
    i = 0
  return retval
            
def main():
    """Script entry point"""
    print("Hello World")
    answer = 0

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    lines = file_input.read().splitlines()
#    for line in lines:
#        print("Line: %s" %(line) )

    answer = process_lines(lines)

    print("Answer 1 %d" % (answer) )

#    for line in lines:
#        print("Line: %s" %(line) )

if __name__ == "__main__":
    main()
