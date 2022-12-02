#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def translate(value):
# A X Rock
# B Y Paper
# C Z Scissors
    trans_key = {
            "A": "R",
            "B": "P",
            "C": "S",
            "X": "R",
            "Y": "P",
            "Z": "S"
            }
    return trans_key[value]

def i_win(oppon, mine):
    #print("Oppon: %s Mine: %s" % ( oppon, mine) )
    if mine == "R" and oppon == "S":
        return True
    if mine == "P" and oppon == "R":
        return True
    if mine == "S" and oppon == "P":
        return True
    return False

def play(oppon, mine):
    win = 0
# A X Rock
# B Y Paper
# C Z Scissors

    #grade my choice
    if mine == "X":
        #print("Rock: 1")
        win += 1
    elif mine == "Y":
        #print("Paper: 2")
        win += 2
    elif mine == "Z":
        #print("Scissor: 3")
        win += 3

    mine = translate(mine)
    oppon = translate(oppon)
    #play game
    if oppon == mine:
        win += 3
    elif i_win(oppon, mine):
        win += 6
    return win

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0

    file_input = open(sys.argv[1], "r")

    for line in file_input:
        line = line.strip("\n")
        #print("Line: %s" % (line) )
        oppon, mine = line.split(" ")
        #print("Opponent: %s Mine: %s" % (oppon, mine ) )
        answer += play(oppon, mine)

    print("Answer: %d" % (answer) )

if __name__ == "__main__":
    main()
