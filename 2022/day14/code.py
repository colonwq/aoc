#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys
def build_segments(lines):
    '''Process lines to build a list of line segments'''
    segments = []

    for line in lines:
        #strip out the ->
        line = line.replace(" ->", "")
        #print("Line: %s" %(line) )
        points = line.split(" ")
        first_point = points.pop(0)
        for second_point in points:
            #print("Segment: %s -> %s"%(first_point, second_point))
            x1,y1 = first_point.split(",")
            x2,y2 = second_point.split(",")
            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)
            #print("Segment: %d,%d -> %d,%d"%(x1,y1,x2,y2))
            segment = [[x1,y1], [x2,y2]]
            segments.append(segment)
            first_point = second_point
    #print("")
    #for segment in segments:
    #    print("segment: %d,%d -> %d,%d" %( segment[0][0], segment[0][1],segment[1][0],segment[1][1]))

    return segments

def find_bounds(segments):
    '''take a list of line segments
    return the min x and max x and
    min y and max y'''
    bounds = []

    max_x = -1
    min_x = float('inf')
    max_y = -1
    min_y = float('inf')

    for segment in segments:
        for point in segment:
            #print("finding min max of X: %d"%(point[0]))
            max_x = max(max_x, point[0])
            min_x = min(min_x, point[0])
            max_y = max(max_y, point[1])
            min_y = min(min_y, point[1])

    return [min_x-1, max_x+1, min_y, max_y]

def build_grid(cols, rows):
    '''build and fill a grid with 0's
    of rows by cols'''

    grid = []
    i = 0
    while i < rows:
        #row = [" "]*cols
        row = ["."]*cols
        grid.append(row)
        i+=1
    return grid 

def sort_segments(segments):
    '''fill the grid with the line segments'''
    for segment in segments:
        if segment[0][0] == segment[1][0]:
            if segment[0][1] > segment[1][1]:
                tmp = segment[1][1]
                segment[1][1] = segment[0][1]
                segment[0][1] = tmp
        if segment[0][1] == segment[1][1]:
            if segment[0][0] > segment[1][0]:
                tmp = segment[1][0]
                segment[1][0] = segment[0][0]
                segment[0][0] = tmp
        #print("segment: %d,%d -> %d,%d" %( segment[0][0], segment[0][1],segment[1][0],segment[1][1]))
    return segments

def print_grid(grid):
    '''basic function to print the grid'''
    #print("The grid has %d rows" %(len(grid)))
    #print("The grid has %d cols" %(len(grid[0])))
    j = 0
    #print( "    0    1")
    while j < len(grid[0]):
        print("%d"% (j%10), end="")
        #print("   %d"% (j), end="")
        j+=1
    print("")
    j = 0
    for row in grid:
        #print(j, row)
        for cell in row:
            print(cell,end="")
        print("")

        j+=1

def draw_segments(grid, segments, offset):
    '''fill in the grid with the passed segments'''
    for segment in segments:
        #print("segment: %d,%d -> %d,%d" %( segment[0][0], segment[0][1],segment[1][0],segment[1][1]))
        #print("segment: %d,%d -> %d,%d" %( segment[0][0]-offset, segment[0][1],segment[1][0]-offset,segment[1][1]))

        if segment[0][0] == segment[1][0]:
            col = segment[0][0] - offset

            i = segment[0][1]
            while i <= segment[1][1]:
                #print("Drawing: %d, %d" %(col,i))
                grid[i][col] = "#"
                i += 1
        else:
            row = segment[0][1]
            i = segment[0][0] - offset

            while i <= segment[1][0] - offset:
                #print("Drawing: %d, %d" %(i, row))
                grid[row][i] = "#"
                i += 1
        #print_grid(grid)

    return grid

def drop_sand(grid, offset):
    '''drop sand at 500,0'''
    print("Dropping sand at %d %d"% (500-offset, 0))
    #grid[0][500-offset] = " "
    print_grid(grid)

    grains = 0
    row = 0
    col=500-offset
    stopped = False
    while not stopped:
        #print("Cur %d, %d %d" % (row,col,grains))
        if row == len(grid)-1:
            print("falling off the bottom")
            return grid, grains

        #if grid[row+1][col] == " ":
        if grid[row+1][col] == ".":
            row += 1
        #elif grid[row+1][col-1] == " ":
        elif grid[row+1][col-1] == ".":
            row += 1
            col -= 1
        #elif grid[row+1][col+1] == " ":
        elif grid[row+1][col+1] == ".":
            row += 1
            col += 1
        #elif row > len(grid) or col < 0 or col > len(grid[0]):
        else:
            #stopped = True
            grid[row][col] = "0"
            row = 0
            col=500-offset
            grains += 1
            #print_grid(grid)


    return grid, grains

def main():
    """Script entry point"""
    print("Hello World")
    answer = 0
    segments = []

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()

    lines = file_input.read().splitlines()

    segments = build_segments(lines)
    
    bounds = find_bounds(segments)
    print("Bounds ", bounds)

    offset = bounds[0]
    print("offset: %d" % (offset))
    cols = bounds[1] - bounds[0] + 1
    rows = bounds[3] + 1

    print("Number of rows: %d Cols: %d" %(rows,cols))

    grid = build_grid(cols, rows)

    segments = sort_segments(segments)

    grid = draw_segments(grid, segments, offset)

    #i = 0
    #while i < 24:
    #    grid, count = drop_sand(grid, offset)
    #    i += 1
    grid, count = drop_sand(grid, offset)
    print("Count: %d" %(count))

    #print_grid(grid)
    answer = count
    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
