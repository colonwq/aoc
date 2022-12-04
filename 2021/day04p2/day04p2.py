#!/usr/bin/python3.6
import numpy as np
import re

IF = open("../day04.data")
#IF = open("../day04.example")
numbers = []
bingonumbercards = []
bingomarkedcards = []

def buildCards():
#{{{
    bingocard = np.empty([5,5], dtype=int)
    bingomarkedcard = np.empty([5,5], dtype=int)
    i = j = 0
    for line in IF:
        line = line.rstrip("\r\n")
        line = line.lstrip()
        if line == "":
            #print("")
            #print("Build a new card")
            bingonumbercards.append(bingocard)
            bingomarkedcards.append(bingomarkedcard)
            bingocard = np.empty([5,5], dtype=int)
            bingomarkedcard = np.empty([5,5], dtype=int)
            i = j = 0
            continue
            print("Next line of code")
        #print("line: %s." % (line) )

        parts = re.split(" +",line)
        for part in parts:
            #print("Part: %d" % (int(part)) )
            #print("Part: %s" % (part) )
            bingocard[i][j] = int(part)
            bingomarkedcard[i][j] = 0
            j += 1
        i += 1
        j = 0
    
    #print("line: %s" % (line) )
    bingonumbercards.append(bingocard)
    bingomarkedcards.append(bingomarkedcard)
#}}}

def markCard( cardidx, i , j ):
#{{{
    #print("Marking Card %d at [%d][%d]" % (cardidx, i, j) )
    bingomarkedcards[cardidx][i][j] = 1
#}}}

def updateCard( cardidx, number):
#{{{
    i = j = 0
    #print("Need to check card for number %d" % (number) ) 
    while i < 5:
        while j < 5:
            #print("Target number[%d,%d]: %d Check Number: %d" % ( i, j , bingonumbercards[cardidx][i][j], number ))
            if bingonumbercards[cardidx][i][j] == number:
                #print("Match found: Card: %d i=%d j=%d num: %d" % ( cardidx, i , j, number ))
                return [ i , j ]
            j += 1
        j = 0
        i += 1
    return [ -1, -1 ]
#}}}

def updateCards(incall):
#{{{
    #print("Incall number %d" % (incall) )
    #print("Number of Bingo Cards: %d" % ( len(bingonumbercards) ) )
    cardidx = 0
    while cardidx < len( bingonumbercards) :
        [i,j] = updateCard(cardidx , incall)
        #print("Found index is [%d,%d]" % (i,j) )
        if i > -1:
            markCard( cardidx, i, j)
        cardidx += 1
#}}}

def checkWinner(cardidx):
#{{{
    i = j = 0
    test = 0
    # test rows
    while i < 5:
        #print("Testing Card %d row %d (j=%d)" % ( cardidx, i, j ) )
        test = bingomarkedcards[cardidx][i][0] + bingomarkedcards[cardidx][i][1] + bingomarkedcards[cardidx][i][2] + bingomarkedcards[cardidx][i][3] + bingomarkedcards[cardidx][i][4]
        if test == 5:
            #print( "Card %d is a WINNER on row %d " % (cardidx, i ) )
            return cardidx
        else:
        #   print("Test: %d" % (test))
            i += 1
    i = 0
    # test columns
    while j < 5:
        #print("Testing Card %d column %d (i=%d)" % ( cardidx, j, i ) )
        test = bingomarkedcards[cardidx][0][j] + bingomarkedcards[cardidx][1][j] + bingomarkedcards[cardidx][2][j] + bingomarkedcards[cardidx][3][j] + bingomarkedcards[cardidx][4][j]
        if test == 5:
            #print( "Card %d is a WINNER on column %d" % (cardidx, j) )
            return cardidx
        else:
            #print("Test: %d" % (test))
            j += 1

    return -1
#}}}

def printCard(cardidx):
#{{{
    i = 0
    print( "Printing Marked Card %d" % (cardidx) )
    while i < 5:
        print("%d %d %d %d %d" % (bingomarkedcards[cardidx][i][0], bingomarkedcards[cardidx][i][1],bingomarkedcards[cardidx][i][2],bingomarkedcards[cardidx][i][3],bingomarkedcards[cardidx][i][4]) )
        i += 1

#}}}

def checkWinners():
#{{{
    i = j = cardidx = 0
    #print("Checking for winning card in %d cards" % (len( bingonumbercards)) )
    while cardidx < len( bingonumbercards) :
        #print( "Checking card %d" % ( cardidx) )
        #printCard(cardidx)
        winner = checkWinner(cardidx)
        if winner > -1:
            #printCard(cardidx)
            return cardidx
        cardidx += 1

    return -1 
#}}}

def sumCard( cardidx ):
#{{{
    i = j = 0
    cardSum = 0
    print( "Summing Marked Card %d" % (cardidx) )
    while i < 5:
        while j < 5:
            if bingomarkedcards[cardidx][i][j] == 0:
                cardSum += bingonumbercards[cardidx][i][j]
            j += 1
        j = 0
        i += 1
    return cardSum

#}}}

#read in the first line and create the list of call numbers
line = IF.readline() 
lineparts = line.split(",")
for part in lineparts:
    numbers.append( int(part) )

#print("Numbers: ", numbers )

#eat a junk line. I guess I could have passed it into
#buildCards but I would have to rework my new card logic.
junk = IF.readline()

buildCards()

print("Number of cards: %d" % (len(bingonumbercards) ) )

callcount = 0
winner = -1
for call in numbers:
    #print("Call number: %d" % (call) )
    callcount += 1
    updateCards(call)
    if callcount >4:
        #print("Check for winner")
        winner = checkWinners()
        while winner > -1:
            #print("Found a winner in card %d" % (winner) )
            if len(bingonumbercards) > 1:
                bingonumbercards.pop(winner)
                bingomarkedcards.pop(winner)
                #print("Number of cards: %d" % (len(bingonumbercards) ) )
            else:
                #printCard(winner)
                cardSum = sumCard( winner)
                print( "Final Number: %d" % (call) )
                print( "Card sum: %d" % (cardSum) )
                print( "Answer: %d" % (call * cardSum) )
                exit()
            winner = checkWinners()

