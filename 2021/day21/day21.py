#!/usr/bin/python3
'''
AoC day 21. Shall we play a game
'''

#import re
#import numpy as np

def main():
    '''
    Here be the magic dragons
    '''
    roll_count = 0
    p1_score = 0
    p2_score = 0
    #data
    p1_position = 2
    p2_position = 0
    #demo
    #p1_position = 3
    #p2_position = 7
    die = 0
    finished = False

    #while not finished and game_round < 5:
    while not finished:
        print("Play a game round %d"%(roll_count))
        #player 1 is first
        d1_1 = die + 1
        die = (die+1)%100
        d1_2 = die + 1
        die = (die+1)%100
        d1_3 = die + 1
        die = (die+1)%100
        print("D1 Total: %d"%(d1_1+d1_2+d1_3))
        p1_position += d1_1 + d1_2 + d1_3
        p1_position %= 10
        roll_count += 3
        p1_score += (p1_position+1)
        print("Player 1 roles %d+%d+%d and moves to space %d for a score of %d"
                %(d1_1,d1_2,d1_3, p1_position, p1_score))
        if p1_score >= 1000:
            finished = True
            continue
        d2_1 = die + 1
        die = (die+1)%100
        d2_2 = die + 1
        die = (die+1)%100
        d2_3 = die + 1
        die = (die+1)%100
        #print("D2: %d"%(d2)
        print("D2 Total: %d"%(d2_1+d2_2+d2_3))
        p2_position += d2_1 + d2_2 + d2_3
        p2_position %= 10
        #print("P1 position: %d"%(p1_position+1))
        #print("P2 position: %d"%(p2_position+1))
        roll_count += 3
        p2_score += (p2_position+1)
        print("Player 2 roles %d+%d+%d and moves to space %d for a score of %d"
                %(d2_1,d2_2,d2_3, p2_position, p2_score))
        if p2_score >= 1000:
            finished = True
            continue
        #print("P1 score: %d\nP2 score:%d"%(p1_score, p2_score))

        #print("Game round: %d"%(roll_count))
        #exit()

    looser = min(p1_score, p2_score)
    print("Die roll: %d"%(roll_count))
    print("Loosing score: %d"%(looser))
    answer = roll_count * looser
    print("Answer: %d"%(answer))
    print("Wrong answer: 995904. Too high")

if __name__ == "__main__":
    main()
