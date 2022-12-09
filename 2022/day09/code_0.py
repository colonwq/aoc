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
            print(cell, end='')
        print("")


def move_down(the_map, h_row, h_col, t_row, t_col, amount):
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    #print("Move down called (%d)" %(amount))
    i = 0
    while i < amount:
        h_row += 1
        if abs(h_row-t_row) > 1:
            print("Need to move tail")
            if h_col == t_col:
                t_row += 1
            elif h_col > t_col:
                t_row += 1
                t_col += 1
            else:
                t_row += 1
                t_col -= 1
            #print("t_col: %d"%(t_col))
            if t_col == len(the_map[0]):
                #print("Need to add a column to the right")
                j = 0
                while j < len(the_map):
                    the_map[j].append(".")
                    j+=1
            if t_row == len(the_map):
                #print("Need to add a row on the bottom")
                the_map.append(["."]*len(the_map[0]))
            the_map[t_row][t_col] = "X"
        i += 1

    return the_map, h_row, h_col, t_row, t_col

def move_up(the_map, h_row, h_col, t_row, t_col, amount):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    #print("Move up called %d" %(amount))
    i = amount
    amount = 0

    while i > amount:
        h_row-=1
        if abs(h_row-t_row) > 1:
            #print("Need to move the tail")
            if h_col == t_col:
                #print("tail in column")
                t_row -= 1
                #the_map[t_row][t_col] = 1
            elif h_col>t_col:
                t_row -= 1
                t_col += 1
                #the_map[t_row][t_col] = 1
            else:
                t_row -= 1
                t_col -= 1
                #the_map[t_row][t_col] = 1
            #print("t_col: %d t_row: %d row_len: %d"%(t_col, t_row, len(the_map[0])))
            j = 0
            if t_col == len(the_map[0]):
                while j < len(the_map):
                    the_map[j].append(".")
                    j+=1
            the_map[t_row][t_col] = "X"

        i-=1


    return the_map, h_row, h_col, t_row, t_col
#}}}

def move_right(the_map, h_row, h_col, t_row, t_col, amount):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    #print("Move right called (%d)" %(amount))

    i = 0
    while i < amount:
        #move head
        h_col+=1
        #check if tail needs to move
        if abs(h_col - t_col) > 1:
            if h_row == t_row:
                #print("Need to move the tail")
                t_col += 1
                #the_map[t_row][t_col] = 1
            elif h_row > t_row:
                t_col += 1
                t_row += 1
                #the_map[t_row][t_col] = 1
            else:
                t_col += 1
                t_row -= 1
                #the_map[t_row][t_col] = 1
            #print("t_col: %d t_row: %d row len: %d" %(t_col, t_row, len(the_map[0])))
            if t_row == len(the_map):
                #print("Need to add a row on the bottom")
                the_map.append(["."]*len(the_map[0]))
            if t_col == len(the_map[0]):
                #print("Need to add a column on the right")
                j = 0
                while j < len(the_map):
                    the_map[j].append(".")
                    j+=1
            the_map[t_row][t_col] = "X"
        i += 1
    #print("Final h_col: %d"%(h_col)) 

    return the_map, h_row, h_col, t_row, t_col
#}}}

def move_left(the_map, h_row, h_col, t_row, t_col, amount):
#{{{
    '''move h_row, h_col by amount
    update t_row, t_col with final location
    update the_map visitation
    '''
    #print("Move left called")
    i = amount
    amount = 0

    while i > amount:
        h_col -= 1
        if abs(h_col-t_col) > 1:
            if h_row == t_row:
                t_col -= 1
            elif h_row > t_row:
                t_col -= 1
                t_row += 1
            else:
                t_col -= 1
                t_row -= 1
            #print("t_row: %d"%(t_row))
            if t_row == len(the_map):
                the_map.append([0]*len(the_map[0]))
            the_map[t_row][t_col] = "X"
        i-=1
    return the_map, h_row, h_col, t_row, t_col
#}}}

def count_tails(the_map):
    '''walk the map
    count all the places the tail has been'''
    answer = 0
    for row in the_map:
        for cell in row:
            if cell != ".":
                answer += 1
    return answer

def move_rope(movements):
    '''this function will move the rope
    head and tail around the map.
    The head moves UDLR.
    The tail moves UDLR and diagonally
    as needed to stay touching.
    Return the number of spots the tail visits.
    '''

    the_map = []
    answer = 0

    i = 0
    #map_size = 300
    map_size = 30
    while i < map_size+30:
        the_map.append(["."]*map_size)
        i += 1
    #print(the_map)
    rows = len(the_map)
    cols = len(the_map[0])

    h_row = int(map_size/2)
    h_col = int(map_size/2)

    t_row = h_row+20
    t_col = h_col+10

    the_map[h_row][h_col] = "X"

    #print_map(the_map)

    for movement in movements:
        #print("Move: %s Amount: %d" %(movement[0], movement[1]))
        dir = movement[0]
        amount = movement[1]
        i = 0
        if dir == "U":
            #print("Up")
            while i < amount:
                i+=1
                the_map, h_row, h_col, t_row, t_col = move_up(the_map, h_row, h_col, t_row, t_col, 1)
            #print_map(the_map)
        elif dir == "D":
            #print("Down")
            while i < amount:
                i+=1
                the_map, h_row, h_col, t_row, t_col = move_down(the_map, h_row, h_col, t_row, t_col, 1)
        elif dir == "L":
            #print("Left")
            while i < amount:
                i+=1
                the_map, h_row, h_col, t_row, t_col = move_left(the_map, h_row, h_col, t_row, t_col, 1)
            #print_map(the_map)
        elif dir == "R":
            #print("Right")
            while i < amount:
                i+=1
                the_map, h_row, h_col, t_row, t_col = move_right(the_map, h_row, h_col, t_row, t_col, 1)
            #print_map(the_map)
        else:
            print("Error")

        #print_map(the_map)
        #print("")

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
