#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def process_line( line = "" ):
  retval = 0
  winners = set()
  picks = set()

  (card, poss_numbers) = line.split(": ")
  (winners, picks) = poss_numbers.split("| ")
  card = card.replace("  ", " ")
  card = card.replace("Card ", "")
  card = card.strip()
  card = card.lstrip()
  winners = winners.replace("  ", " ").strip().lstrip()
  picks = picks.replace("  ", " ").strip().lstrip()
  print("Card: .", card,". Winners: .", winners , ". Picks: .", picks,".")

  winners_set = set(winners.split(" "))
  picks_set = set(picks.split(" "))
  
  print("Card: ", card," Winners: ", winners_set , " Picks: ", picks_set)
  matches = winners_set.intersection(picks_set)
  print("Matches: ", matches, " Number of matches: %d" %(len(matches)))
  if len(matches)>0:
    retval = 1
    i = 1
    while i < len(matches):
      retval *= 2
      i += 1
  print("Card winnings: %d" %(retval))
  print("")
#  print("Line: %s"%(line))
  return retval


def main():
    """Script entry point"""
    print("Hello World")
    print("853: too low")
    print("23795: too high")
    print("21138: just right")
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
        print("Line: %s." %(line) )
        answer += process_line(line)

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
