#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def count_trees(tree_map, drop=3, slide=1):
    '''
    this function will 'ski' down the map
    with fixed slope and count trees unilt the
    bottom is reached
    '''
    rows = len(tree_map)
    cols = len(tree_map[0])
    row = int(0)
    col = int(0)
    trees = 0

    #print("Tree map: " , tree_map)
    #for s_row in tree_map:
    #    print(s_row)
    rows = len(tree_map)
    cols = len(tree_map[0])
#    print("Rows: %d Cols: %d" % ( rows, cols) )
#    print("Start Row: %d Start Cols: %d" % ( row, col) )
    while row < rows-1:
        col += drop
        col %= cols
        row += slide
        #print("Looking at Rows: %d Cols: %d" % ( row, col) )
        if tree_map[row][col] == '#':
            trees += 1
    print("Trees:%d"% ( trees) )
    return trees


def main():
    """Script entry point"""
    print("Hello World")
    answer = 1
    #file_input = open(sys.argv[1], "r")
    tree_map = []
    slopes = [ [1,1], [3,1], [5,1], [7,1], [1,2] ]
    print(slopes)
    #sys.exit()

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
        #print("Line: %s"% (line) )
        tree_map.append(line)
    #answer = count_trees(tree_map)

    for slope in slopes:
        print("Slide: %d Drop: %d" %(slope[0],slope[1]) )
        answer *= count_trees(tree_map, drop=slope[0], slide=slope[1] )
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
