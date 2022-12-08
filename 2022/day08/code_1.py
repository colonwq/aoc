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
    count_up = 0
    while cur_row >= 0:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking UP at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree < cur_tree:
            count_up += 1
        elif look_tree >= cur_tree:
            count_up += 1
            cur_row = -1
        cur_row -= 1
    #print("Tree: %d (%d,%d):Count up: %d" %(cur_tree,i,j, count_up))
    #look left
    cur_row = i
    cur_col = j-1
    count_left = 0
    while cur_col >= 0:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking LEFT at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree < cur_tree:
            count_left += 1
        elif look_tree >= cur_tree:
            count_left += 1
            cur_col = -1
        cur_col -= 1
    #print("Tree: %d (%d,%d):count left: %d" %(cur_tree,i,j, count_left))
    #look down
    cur_col = j
    cur_row = i+1
    count_down = 0
    while cur_row < rows:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking DOWN at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree < cur_tree:
            count_down += 1
        elif look_tree >= cur_tree:
            count_down += 1
            cur_row = rows
        cur_row += 1
    #print("Tree: %d (%d,%d):Count down: %d" %(cur_tree,i,j, count_down))
    #look right
    cur_row = i
    cur_col = j+1
    count_right = 0
    while cur_col < cols:
        look_tree = tree_map[cur_row][cur_col] 
        #print("Looking RIGHT at (%d:%d): %d"% (cur_row, cur_col, look_tree))
        if look_tree < cur_tree:
            count_right += 1
        elif look_tree >= cur_tree:
            count_right += 1
            cur_col = cols
        cur_col += 1
    #print("Tree: %d (%d,%d):Count right: %d" %(cur_tree,i,j, count_right))

    count = count_up * count_down * count_left * count_right

    #print("Return Count: (%d,%d) %d Count: "% (i,j,cur_tree), count)

    return count

def process_tree_map(tree_map):
    '''this function will check each tree
    and count it if there are shorter trees
    between it and the edge
    '''
    answer = 0

    rows = len(tree_map)
    cols = len(tree_map)

    #print("Map size: Rows: %d Cols: %d" %(rows, cols))

    #answer += rows + rows + cols + cols - 4

    i = 1
    while i < rows-1:
        j = 1
        while j < cols -1:
            tree_map[i][j] = tree_map[i][j]
            #print("(%d,%d) %d "% (i,j,tree_map[i][j]), end="")
            answer = max(check_loc(tree_map, i , j),answer)
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

    answer = max(answer,process_tree_map(tree_map))

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
