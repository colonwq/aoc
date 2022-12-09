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
        print(row)

def print_rope(ropes):
    '''this will print the locations of the ropes'''
    for rope in ropes:
        row = rope[0]
        col = rope[1]
        print("Row: %d Col %d" %(row, col))


def move_down(the_map, h_row, h_col, t_row, t_col, amount=1, ropes=[]):
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move down called")
#    h_row += 1
#    if abs(h_row-t_row) > 1:
#        print("Need to move tail")
#        if h_col == t_col:
#            t_row += 1
#        elif h_col > t_col:
#            t_row += 1
#            t_col += 1
#        else:
#            t_row += 1
#            t_col -= 1
#        #print("t_col: %d"%(t_col))
#    the_map[t_row][t_col] = 1

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
    the_map[last_row][last_col] = 1

    print_rope(ropes)

    return the_map, h_row, h_col, t_row, t_col

def move_up(the_map, h_row, h_col, t_row, t_col, amount=1, ropes=[]):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move up called")
    h_row-=1
#    if abs(h_row-t_row) > 1:
#        #print("Need to move the tail")
#        if h_col == t_col:
#            #print("tail in column")
#            t_row -= 1
#            #the_map[t_row][t_col] = 1
#        elif h_col>t_col:
#            t_row -= 1
#            t_col += 1
#            #the_map[t_row][t_col] = 1
#        else:
#            t_row -= 1
#            t_col -= 1
#            #the_map[t_row][t_col] = 1
#        #print("t_col: %d t_row: %d row_len: %d"%(t_col, t_row, len(the_map[0])))
#    the_map[t_row][t_col] = 1

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
            if abs(ropes[i-1][0]-ropes[i][0]) > 1:
                #print("Movement")
                ropes[i][0] -= 1
                if ropes[i-1][1] > ropes[i][1]:
                    ropes[i][1] += 1
                elif ropes[i-1][1] < ropes[i][1]:
                    ropes[i][1] -= 1
        i+=1
    last_row = ropes[-1][0]
    last_col = ropes[-1][1]
    print("Setting Last row: %d Last col: %d" %(last_row, last_col))
    the_map[last_row][last_col] = 1

    print_rope(ropes)

    return the_map, h_row, h_col, t_row, t_col
#}}}

def move_right(the_map, h_row, h_col, t_row, t_col, amount=1, ropes=[]):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move right called")

    #h_col+=1
    ##check if tail needs to move
    #if abs(h_col - t_col) > 1:
    #    if h_row == t_row:
    #        t_col += 1
    #    elif h_row > t_row:
    #        t_col += 1
    #        t_row += 1
    #    else:
    #        t_col += 1
    #        t_row -= 1
    #    #print("t_col: %d t_row: %d row len: %d" %(t_col, t_row, len(the_map[0])))
    #    the_map[t_row][t_col] = 1
    ##print("Final h_col: %d"%(h_col)) 


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
    last_row = ropes[-1][0]
    last_col = ropes[-1][1]
    print("Setting Last row: %d Last col: %d" %(last_row, last_col))
    the_map[last_row][last_col] = 1

    print_rope(ropes)

    return the_map, h_row, h_col, t_row, t_col
#}}}

def move_left(the_map, h_row, h_col, t_row, t_col, amount=1, ropes=[]):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    print("Move left called")
#    h_col -= 1
#    if abs(h_col-t_col) > 1:
#        if h_row == t_row:
#            t_col -= 1
#        elif h_row > t_row:
#            t_col -= 1
#            t_row += 1
#        else:
#            t_col -= 1
#            t_row -= 1
#    the_map[t_row][t_col] = 1

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
    the_map[last_row][last_col] = 1

    print_rope(ropes)

    return the_map, h_row, h_col, t_row, t_col
#}}}

def count_tails(the_map):
    '''walk the map
    count all the places the tail has been'''
    answer = 0
    for row in the_map:
        for cell in row:
            answer += cell
    return answer

def move_rope(movements):
    '''this function will move the rope
    head and tail around the map.
    The head moves UPLR.
    The tail moves UPLR and diagonlly
    as needed to stay touching.
    Return the number of spots the tail visits.
    '''

    the_map = []
    answer = 0

    i = 0
    #map_size = 500
    map_size = 30
    while i < map_size:
        the_map.append([0]*map_size)
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
    #print("Ropes: ", ropes)

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
                the_map, h_row, h_col, t_row, t_col = move_up(the_map, h_row, h_col, t_row, t_col, ropes=ropes )
        #    print_map(the_map)
        elif dir == "D":
            while i < amount:
                i+=1
                the_map, h_row, h_col, t_row, t_col = move_down(the_map, h_row, h_col, t_row, t_col, ropes=ropes )
        #    print_map(the_map)
        elif dir == "L":
            while i < amount:
                i+=1
                the_map, h_row, h_col, t_row, t_col = move_left(the_map, h_row, h_col, t_row, t_col, ropes=ropes )
        #    print_map(the_map)
        elif dir == "R":
            while i < amount:
                i+=1
                the_map, h_row, h_col, t_row, t_col = move_right(the_map, h_row, h_col, t_row, t_col, ropes=ropes )
        #    print_map(the_map)
        else:
            print("Error")

    print_map(the_map)

    answer = count_tails(the_map)
    return answer

def main():
    """Script entry point"""
    print("Hello World")
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
