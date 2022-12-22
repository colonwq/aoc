#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def strip_lines(lines):
    '''strip down the input lines to basic 
    values SX,SY,BX,BY'''

    new_lines = []

    for line in lines:
        #print("Line: %s" %(line) )
        line = line.replace("Sensor at x=","")
        line = line.replace(" y=","")
        line = line.replace(": closest beacon is at ","")
        line = line.replace("x=",",")
        new_lines.append(line)

    return new_lines

def build_points_distance(lines):
    '''take a pair of points
    builds a list of first point and positive distance
    to the second

    example 2,18 -> -2,15 returns 2,18,7
    '''
    points_distance = []

    for line in lines:
        pd = []
        points = line.split(",")
        #print("Points: ", points)
        pd.append(int(points[0]))
        pd.append(int(points[1]))

        x_dist = abs(int(points[0])-int(points[2]))
        y_dist = abs(int(points[1])-int(points[3]))
        pd.append(x_dist+y_dist)
        #print("point_distance: ", pd)

        points_distance.append(pd)

    return points_distance

def check_line(points_distance, row):
    '''check each of the rows in points,distance 
    to see if they intersect the row of interest
    in part 1 test this row is 10
    in part 1 this row is 2000000
    I think the amount of coverage is a knight movement based off the
    off set of the row in interest
    '''
    count = 0

    #print("Row of interest: %d"%(row))

    row_covered = {}

    for my_col, my_row, my_dist in points_distance:
        min_row = my_row - my_dist
        max_row = my_row + my_dist
        if row >= min_row and row <= max_row:
            #print("Col: %d, Row: %d, Dist: %d" %(my_col,my_row,my_dist) )
            row_dist = my_dist
            col_dist = 0
            if row >= my_row:
                #print("My Row higher than row of interested")
                while my_row+row_dist >= row:
                    row_covered[my_col-col_dist] = 1
                    row_covered[my_col+col_dist] = 1
                    row_dist -= 1
                    col_dist += 1
            if row <= my_row:
                #print("My Row lower than row of interested")
                while my_row-row_dist <= row:
                    row_covered[my_col-col_dist] = 1
                    row_covered[my_col+col_dist] = 1
                    row_dist -= 1
                    col_dist += 1
    count = len(row_covered.keys())
    #print("Row covered: %d"%(count))

    return count

def check_uncovered(points, dimension):
    '''interate through the rows
    check each sensor points and distance
    return rows not covered by a sensor->distance'''
    uncovered_rows = {}
    '''
    XXX I feel this is the right path. 
    - for each row col point
        for each sensor
            do an and of:
              a) quick check to see if the point is not in the inner half of a sensor 
              ie sensor points +- 1/2 dist
              b) Do the hard check to see if the row, col is not covered
              by the rest of the sensor coverage.

              if not covered, return row col
              if coverd, go to next sensor
         
    '''

    for row in range(dimension):
        for col in range(dimension):
            possible = True
            for srow, scol, sdist in points:
                srmin = srow-sdist
                srmax = srow+sdist
                scmin = scol-sdist
                scmax = scol+sdist
                loc = str(row)+","+str(col)
                if (row >= srmin and row <= srmax) or (col >= scmin and col <= scmax):
                    possible = False
            if possible:
                print("Row %d Col %d" %(row, col))



def find_row_bounds(points):
    '''interate through the points and find the min/max'''
    '''I could shortenthis to just the points overlapping 
    the row of interest'''
    #XXX Need to find the width of the row
    #start is min(x-dist) for each point_distance
    #end is max(x+dist) for each point_distance
    row_max = -float('inf')
    row_min = float('inf')

    for point in points:
        row_max = max(row_max,point[1]+point[2])
        row_min = min(row_min,point[1]-point[2])

    return row_min, row_max

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0

    points_distance = []

    try:
        file_input = open(sys.argv[1], "r")
    except IndexError as i_exception:
        print("No file given: ", i_exception)
        sys.exit()
    except FileNotFoundError as f_exception:
        print("File not found: ", f_exception)
        sys.exit()
    
    lines = file_input.read().splitlines()

    lines = strip_lines(lines)

    #for line in lines:
    #    print("Line: %s" %(line) )

    points_distance = build_points_distance(lines)

    #for srow, scol, sdist in points_distance:
    #    smin = srow-sdist
    #    smax = srow+sdist
    #    print("row range %d -> %d" %(smin, smax))

    (row_min,row_max) = find_row_bounds(points_distance)

    #answer = check_line(points_distance, int(sys.argv[2]))

    uncovered = check_uncovered(points_distance, int(sys.argv[2]))
    #print("Uncovered: %d"%(len(uncovered)))

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
