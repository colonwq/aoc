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
  print("Processing: %s" %(line))
  (game,results) = line.split(":")
  game = int(game.replace("Game ",""))
  print( "playing game: %d" % (game))
  results = results.replace(";", ",")
  #print("Results: %s" % (results))
  parts = results.split(",")
  for part in parts:
    #print("Part: .%s." % (part) )
    (amount, color) = part.strip().split(" ")
    print("Color: %s Amount: %s" %( color, amount))
    if color[0] == 'g' and int(amount) > VALID_GREEN:
      valid_game = False
    elif color[0] == 'r' and int(amount) > VALID_RED:
      valid_game = False
    elif color[0] == 'b' and int(amount) > VALID_BLUE:
      valid_game = False
  if valid_game:
    retval = game
    #print( "played game: %d" % (game))
    print("Valid game: %d" % (retval))
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
    for line in lines:
        #print("Line: %s" %(line) )
        answer += process_line( line ) 

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
