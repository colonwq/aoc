#!/usr/bin/env python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
from collections import defaultdict

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

  winners_set = set(winners.split(" "))
  picks_set = set(picks.split(" "))
  
  matches = winners_set.intersection(picks_set)
  retval = len(matches)
  return retval

def print_seen_count(seen_cards = []):
  print("seen count:")
  for key in sorted(seen_cards):
    print("Key: %s Amount: %d" % (int(key), seen_cards[key]))


def main():
    """Script entry point"""

    my_cards = []
    answer = 0
    seen_cards = defaultdict(int);

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    lines = file_input.read().splitlines()
    for card, line in enumerate(lines):
      print("Looking at line %d (%s)"%(card, line))
      #print("Looking at line %d (%s)"%(index, lines[index]))
      #print("Line: %s." %(lines[index]) )
      winners = process_line(line)
      seen_cards[card] += 1
      if winners > 0:
        for updatecard in range(winners):
           seen_cards[card+1+updatecard] += seen_cards[card]
           
    print_seen_count(seen_cards)
    answer = sum(seen_cards.values())
    print("Wrong answer: 5719359 (too low)")
    print("Answer        %d" % (answer) )

if __name__ == "__main__":
    main()
