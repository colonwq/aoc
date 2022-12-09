#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def print_map(the_map):
    '''this will print the map'''
    for row in the_map:
        #print(row)
        for cell in row:
            print(cell, end="")
        print("")

def print_rope(ropes):
    '''this will print the locations of the ropes'''
    for rope in ropes:
        row = rope[0]
        col = rope[1]
        #print("Row: %d Col %d" %(row, col))
        print("Rope: %d:%d" %(row, col))


def move_down(the_map=[],  amount=1, ropes=[]):
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move down called")

    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    ropes[0][0]+=1
    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    i = 1
    #print("Len of ropes: %d"% (len(ropes)) )
    while i < len(ropes):
        #print("Next segment(%d): %d, %d" %(i,ropes[i][0], ropes[i][1]))
        if (ropes[i-1][0] == ropes[i][0]) and (ropes[i-1][1] == ropes[i][1]):
            #print("No movement")
            pass
        else:
            if abs(ropes[i-1][0]-ropes[i][0]) > 1:
                #print("Movement")
                ropes[i][0] += 1
                if ropes[i-1][1] > ropes[i][1]:
                    ropes[i][1] += 1
                elif ropes[i-1][1] < ropes[i][1]:
                    ropes[i][1] -= 1
        i+=1
    last_row = ropes[-1][0]
    last_col = ropes[-1][1]
    print("Setting Last row: %d Last col: %d" %(last_row, last_col))
    the_map[last_row][last_col] = "X"

    print_rope(ropes)

    return

def move_up(the_map=[], amount=1, ropes=[]):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move up called")

    i=0
    for rope in ropes:
        the_map[rope[0]][rope[1]] = "."
        i+=1
    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    ropes[0][0]-=1
    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    i = 1
    while i < len(ropes):
        print("Rope: %d (%d:%d) Rope: %d (%d:%d)" % (i, ropes[i][0], ropes[i][1], i-1, ropes[i-1][0], ropes[i-1][1]))
        #print("Next segment(%d): %d, %d" %(i,ropes[i][0], ropes[i][1]))
        if (ropes[i-1][0] == ropes[i][0]) and (ropes[i-1][1] == ropes[i][1]):
            #print("No movement")
            pass
        else:
            if abs(ropes[i-1][0]-ropes[i][0]) > 1:
                print("(%d) Move up " %(i), end="")
                ropes[i][0] -= 1
            if ropes[i-1][1] > ropes[i][1]:
                print("Move Right ", end="")
                ropes[i][1] += 1
            elif ropes[i-1][1] < ropes[i][1]:
                print("Move Left ", end="")
                ropes[i][1] -= 1
            print("")
        i+=1
    i=0
    for rope in ropes:
        if i==0:
            the_map[rope[0]][rope[1]] = "H"
        else:
            the_map[rope[0]][rope[1]] = i
        i+=1
    last_row = ropes[-1][0]
    last_col = ropes[-1][1]
    print("Setting Last row: %d Last col: %d" %(last_row, last_col))
    the_map[last_row][last_col] = "X"

    print_rope(ropes)

    return
#}}}

def move_right(the_map=[], amount=1, ropes=[]):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move right called")

    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    ropes[0][1]+=1
    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    i = 1
    while i < len(ropes):
        #print("Next segment(%d): %d, %d" %(i,ropes[i][0], ropes[i][1]))
        if (ropes[i-1][0] == ropes[i][0]) and (ropes[i-1][1] == ropes[i][1]):
            #print("No movement")
            pass
        else:
            if abs(ropes[i-1][1]-ropes[i][1]) > 1:
                #print("Movement")
                ropes[i][1]+=1
                if ropes[i-1][0] > ropes[i][0]:
                    ropes[i][0] += 1
                elif ropes[i-1][0] < ropes[i][0]:
                    ropes[i][0] -= 1
            pass
        i+=1
    i=0
    for rope in ropes:
        the_map[rope[0]][rope[1]] = i
        i+=1
    last_row = ropes[-1][0]
    last_col = ropes[-1][1]
    print("Setting Last row: %d Last col: %d" %(last_row, last_col))
    the_map[last_row][last_col] = "X"

    print_rope(ropes)

    return
#}}}

def move_left(the_map=[], amount=1, ropes=[]):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move left called")

    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    ropes[0][0]-=1
    #print("Rope head: %d, %d" % (ropes[0][0], ropes[0][1]))
    i = 1
    while i < len(ropes):
        #print("Next segment(%d): %d, %d" %(i,ropes[i][0], ropes[i][1]))
        if (ropes[i-1][0] == ropes[i][0]) and (ropes[i-1][1] == ropes[i][1]):
            #print("No movement")
            pass
        else:
            if abs(ropes[i-1][1]-ropes[i][1]) > 1:
                #print("Movement")
                ropes[i][1]-=1
                if ropes[i-1][0] > ropes[i][0]:
                    ropes[i][0] += 1
                elif ropes[i-1][0] < ropes[i][0]:
                    ropes[i][0] -= 1
        i+=1
    last_row = ropes[-1][0]
    last_col = ropes[-1][1]
    print("Setting Last row: %d Last col: %d" %(last_row, last_col))
    the_map[last_row][last_col] = "X"

    print_rope(ropes)

    return
#}}}

def count_tails(the_map):
    '''walk the map
    count all the places the tail has been'''
    answer = 0
    for row in the_map:
        for cell in row:
            if cell == "X":
                answer += 1
    return answer

def move_rope(movements):
    '''this function will move the rope
    head and tail around the map.
    The head moves up/dow/left/right.
    The tail moves up/dow/left/right and diagonally
    as needed to stay touching.
    Return the number of spots the tail visits.
    '''

    the_map = []
    answer = 0

    i = 0
    #map_size = 500
    map_size = 20
    while i < map_size:
        the_map.append(["."]*map_size)
        i += 1
    #print(the_map)
    rows = len(the_map)
    cols = len(the_map[0])

    h_row = int(map_size/2)
    h_col = int(map_size/2)

    t_row = h_row
    t_col = h_col

    the_map[h_row][h_col] = 1
    ropes = []
    #print("Ropes: ", ropes)
    i = 0
    while i < 10:
        #print("i: %d" %(i))
        spot = [t_row,t_col]
        ropes.append(spot)
        i+=1

    #sys.exit()
   

    print_map(the_map)

    print_rope(ropes)

    for movement in movements:
        print("Move: %s Amount: %d" %(movement[0], movement[1]))
        dir = movement[0]
        amount = movement[1]
        i = 0
        if dir == "U":
            while i < amount:
                i+=1
                move_up(the_map=the_map, ropes=ropes )
                print_map(the_map)
        elif dir == "D":
            while i < amount:
                i+=1
                move_down(the_map=the_map, ropes=ropes )
        #    print_map(the_map)
        elif dir == "L":
            while i < amount:
                i+=1
                move_left(the_map=the_map, ropes=ropes )
        #    print_map(the_map)
        elif dir == "R":
            while i < amount:
                i+=1
                move_right(the_map=the_map, ropes=ropes )
        #    print_map(the_map)
        else:
            print("Error")

    print_map(the_map)

    answer = count_tails(the_map)
    return answer

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    movements = []

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    for line in file_input:
        line = line.strip("\n")
        #print("Line: %s" %(line) )
        dir, amount = line.split(" ")
        #print("Direction: %s Amount: %s." %(dir, amount))
        movements.append([dir,int(amount)])

    answer = move_rope(movements)
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
