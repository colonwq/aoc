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
#  if len(matches)>0:
#    retval = 1
#    i = 1
#    while i < len(matches):
#      retval *= 2
#      i += 1
  retval = len(matches)
  #print("Card winnings: %d" %(retval))
  #print("")
#  print("Line: %s"%(line))
  return retval

def print_seen_count(seen_cards = []):
  print("seen count:")
  for key in sorted(seen_cards):
    print("Key: %s Amount: %d" % (int(key)+1, seen_cards[key]))


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
    for i in range(0, len(lines)):
      my_cards.append(i)
    print("Len lines: %d Len my_cards: %s" %( len(lines), len(my_cards)))
    print("")
    while len(my_cards):
        index = my_cards.pop(0)
        #print("Looking at line %d (%s)"%(index, lines[index]))
        #print("Line: %s." %(lines[index]) )
        if index in seen_cards.keys():
          seen_cards[index] += 1
        else:
          seen_cards[index] = 1
        winners = process_line(lines[index])
        if winners > 0:
          print("Winner count for line %d: %d" %(index, winners))
          print("need to add indexes: " , my_cards[:winners])
          for card in my_cards[:winners]:
            if card in seen_cards.keys():
#               print("Adding %d to card %d" %(seen_cards[index], card))
               seen_cards[card] += seen_cards[index]
               #seen_cards[card] += 1
            else:
              seen_cards[card] = 1
#        print_seen_count(seen_cards)

    #print("Seen cards: ", seen_cards)
    #seen_keys = seen_cards.keys()
    for key in sorted(seen_cards):
       answer += seen_cards[key]
       #print("Key: %s Amount: %d" % (int(key)+1, seen_cards[key]))
    #print_seen_count(seen_cards)
#    print("Answer should be:\nKey 1 -> 1\nKey 2 -> 2\nKey 3 -> 4\nKey 4 -> 8\nKey 5 -> 14\nKey 6 -> 1")
    print("Wrong answer: 5719359 (too low)")
    print("Answer        %d" % (answer) )
    print("Len lines: %d Len my_cards: %s" %( len(lines), len(my_cards)))

if __name__ == "__main__":
    main()
