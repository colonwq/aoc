#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def check_loc(tree_map, i, j):
    '''this function will check the adjacent
    rows and columns to see if everything
    is less
    '''
    tallest = 0

    rows = len(tree_map)
    cols = len(tree_map[0])

    cur_tree = tree_map[i][j]
    #print("Current Tree: (%d,%d) %d "% (i,j,cur_tree))
    #look up
    cur_row = i-1
    cur_col = j
    tallest_up = 1
    #look down
    while cur_row >= 0:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree >= cur_tree:
            tallest_up = 0
        cur_row -= 1
    #print("Tree: %d (%d,%d):Tallest up: %d" %(cur_tree,i,j, tallest_up))
    tallest_down = 1
    cur_row = i+1
    while cur_row < rows:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree >= cur_tree:
            tallest_down = 0
        cur_row += 1
    #print("Tree: %d (%d,%d):Tallest down: %d" %(cur_tree,i,j, tallest_down))
    #look left
    tallest_left = 1
    cur_row = i
    cur_col = j-1
    while cur_col >= 0:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree >= cur_tree:
            tallest_left = 0
        cur_col -= 1
    #print("Tree: %d (%d,%d):Tallest left: %d" %(cur_tree,i,j, tallest_left))
    #look right
    tallest_right = 1
    cur_col = j+1
    while cur_col < cols:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree >= cur_tree:
            tallest_right = 0
        cur_col += 1
    #print("Tree: %d (%d,%d):Tallest right: %d" %(cur_tree,i,j, tallest_right))

    tallest = tallest_up or tallest_down or tallest_left or tallest_right

    #print("Current Tree: (%d,%d) %d Tallest: "% (i,j,cur_tree), tallest)

    return tallest

def process_tree_map(tree_map):
    '''this function will check each tree
    and count it if there are shorter trees
    between it and the edge
    '''
    answer = 0

    rows = len(tree_map)
    cols = len(tree_map)

    #print("Map size: Rows: %d Cols: %d" %(rows, cols))

    answer += rows + rows + cols + cols - 4

    i = 1
    while i < rows-1:
        j = 1
        while j < cols -1:
            tree_map[i][j] = tree_map[i][j]
            #print("(%d,%d) %d "% (i,j,tree_map[i][j]), end="")
            answer += check_loc(tree_map, i , j)
            j += 1
        #print("")
        i += 1

    return answer


def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    tree_map = []

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    for line in file_input:
        line = line.rstrip("\n")
        #print("Line: %s" %(line) )
        tree_map.append(list(map(int,line)))

    #for tree_row in tree_map:
    #    print(tree_row)

    answer = process_tree_map(tree_map)

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
