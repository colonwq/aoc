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
  #print("Card: .", card,". Winners: .", winners , ". Picks: .", picks,".")

  winners_set = set(winners.split(" "))
  picks_set = set(picks.split(" "))
  
  #print("Card: ", card," Winners: ", winners_set , " Picks: ", picks_set)
  matches = winners_set.intersection(picks_set)
  #print("Matches: ", matches, " Number of matches: %d" %(len(matches)))
  retval = len(matches)
  #print("Card winnings: %d" %(retval))
  #print("")
#  print("Line: %s"%(line))
  return int(card), retval

def print_seen_count(seen_cards = []):
  print("seen count:")
  for key in sorted(seen_cards):
    print("Key: %s Amount: %d" % (int(key), seen_cards[key]))


def main():
    """Script entry point"""

    my_cards = []
    answer = 0
    seen_cards = dict();

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    lines = file_input.read().splitlines()
    while len(lines) > 0:
      line = lines.pop(0)
      #print("Looking at line %d (%s)"%(index, lines[index]))
      #print("Line: %s." %(lines[index]) )
      card, winners = process_line(line)
      if card in seen_cards:
        seen_cards[card] += 1
      else:
        seen_cards[card] = 1
      if winners > 0:
        print("Winner count for card %d: %d" %(card, winners))
        print("need to add to the next %d cards" %(winners))
        i = 1
        while i <= winners:
          if card+i in seen_cards:
            print("Adding %d to card %d" %(seen_cards[card], card+i))
            seen_cards[card+i] += seen_cards[card]
          else:
            #print("Setting %d to card %d" %(1, seen_cards[card+i]))
            print("Setting %d to card %d" %(1, card+i) )
            seen_cards[card+i] = 1
          i += 1
           
      print_seen_count(seen_cards)
    print_seen_count(seen_cards)
    answer = sum(seen_cards.values())
    print("Wrong answer: 5719359 (too low)")
    print("Answer        %d" % (answer) )

if __name__ == "__main__":
    main()
