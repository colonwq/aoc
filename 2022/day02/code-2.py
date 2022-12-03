#!/usr/bin/python3
'''
Solution for Day02 part 2
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

def my_tie(value):
    if value == "R": #rock is 1
        return 1
    elif value =="P": #paper is 2
        return 2
    else: #scissor is 3
        return 3

def my_loss(value):
    if value == "R": #rocks smashes scissors
        return 3
    elif value == "P": #paper covers rock
        return 1
    else: #scissors cut paper
        return 2

def my_win(value):
    if value == "R": #rock is covered by paper
        #print("I played paper 2")
        return 2
    elif value == "P": #paper is cut by scisor
        #print("I played scissor 3")
        return 3
    else: #scisor is smashed by rock
        #print("I played rock 1")
        return 1

#def i_win(oppon, mine):
#    #print("Oppon: %s Mine: %s" % ( oppon, mine) )
#    if mine == "R" and oppon == "S":
#        return True
#    if mine == "P" and oppon == "R":
#        return True
#    if mine == "S" and oppon == "P":
#        return True
#    return False

def play(oppon, result):
    win = 0
# A X Rock
# B Y Paper
# C Z Scissors

    oppon = translate(oppon)

    if result == "Y":
        #print("A tie")
        win += 3
        win += my_tie(oppon)
    elif result == "Z":
        #print("A win")
        win += my_win(oppon)
        win += 6
    else:
        #print("A loss")
        win += my_loss(oppon)

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
        #print("Opponent: %s Result: %s" % (oppon, mine ) )
        answer += play(oppon, mine)

    print("Wrong answer 11864")
    print("Answer: %d" % (answer) )

if __name__ == "__main__":
    main()
