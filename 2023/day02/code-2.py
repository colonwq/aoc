#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

VALID_RED = 12
VALID_GREEN = 13
VALID_BLUE = 14

def process_line( line = "How: 1 red, 2 blue, 3 green" ):
  retval = 0
  valid_game = True
  max_r = max_g = max_b = -1
  
  #print("Processing: %s" %(line))
  (game,results) = line.split(":")
  game = int(game.replace("Game ",""))
  #print( "playing game: %d" % (game))
  results = results.replace(";", ",")
  #print("Results: %s" % (results))
  parts = results.split(",")
  for part in parts:
    #print("Part: .%s." % (part) )
    (amount, color) = part.strip().split(" ")
    #print("Color: %s Amount: %s" %( color, amount))
    amount = int(amount)
    if color[0] == 'g':
      max_g = max(max_g, amount)
    elif color[0] == 'r':
      max_r = max(max_r, amount)
    elif color[0] == 'b':
      max_b = max(max_b, amount)
  #print("Max r: %d Mar g: %d Max b: %d"%(max_r, max_g, max_b))
  retval = max_r * max_g * max_b
  #print("Returning game: %d" % (retval))
  return retval
  
def main():
    """Script entry point"""
    #print("Hello World")
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
    for line in lines:
        #print("Line: %s" %(line) )
        answer += process_line( line ) 

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
