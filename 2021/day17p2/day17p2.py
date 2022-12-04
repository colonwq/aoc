#!/usr/bin/python3
'''
Day 16 part 1... some kind of protocol decoder
'''

import re

def within_square(my_x, my_y, my_corners):
    '''
    Are x and y within my_corners
    '''
    #if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']:
    #if my_x >= my_corners['x_min']+1 and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']:
    #if my_x >= my_corners['x_min']-1 and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']:
    #if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max']+1 and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']:
    #if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max']-1 and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']:
    #if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max']-1 and my_y >= my_corners['y_min']:
    #if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max']+1 and my_y >= my_corners['y_min']:
    #if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']-1:
    #if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']+1:
    if my_x >= my_corners['x_min'] and my_x <= my_corners['x_max'] and my_y <= my_corners['y_max'] and my_y >= my_corners['y_min']:
        return True
    else:
        return False

def hit_it(x_vect, y_vect, my_corners):
    '''
    Run along each generation of the points along x_vect and y_vect 
    to see if they fall into my_corners. Stop at x_max or y_min
    '''
    x_point = 0
    y_point = 0
    intersect = 0
    while True:
        x_point += x_vect
        y_point += y_vect
        x_vect = max(0, x_vect-1)
        y_vect -= 1
        if within_square(x_point, y_point, my_corners):
            ##print("%d , %d (%d,%d)"%(x_vect, y_vect, x_point, y_point))
            #print("%d , %d"%(x_vect, y_vect))
            #intersect += 1
            return True
        elif x_point > my_corners['x_max'] or y_point < my_corners['y_min']:
            #print("Fell outside")
            #return intersect
            return False
            #break
    #return intersect

def shoot_points(my_corners):
    '''
    I will shoot a range of shots and see if they land in the corners
    I stop the generations if I land in the corners, exceed x_max or
    fall below y_min
    '''
    #print("Shooting a corner")
    a_hit = 0

    for x_vect in range(0, my_corners['x_max']+1):
        for y_vect in range(my_corners['y_min'], -my_corners['y_min']):
            #print("Shooting vect %d:%d"%(x_vect,y_vect))
            #a_hit += hit_it(x_vect, y_vect, my_corners)
            if hit_it(x_vect, y_vect, my_corners):
                #print("%d , %d"%(x_vect, y_vect))
                a_hit += 1
    return a_hit

def main():
    '''
    Here is where dragons occur
    '''
    in_file = open("../day17.data")
    #in_file = open("../day17.demo")

    for line in in_file:
        line = line.rstrip("\r\n")
        #print("Line: %s" % (line))

        line = re.sub("^.*rea: ", "",line)

        #print("Line: %s" % (line))
        [x_s, y_s] = re.split( ", ", line)
        #print("X range: %s" %(x_s))
        #print("Y range: %s" %(y_s))
        x_s = re.sub("x=","", x_s)
        y_s = re.sub("y=","", y_s)
        #print("X range: %s" %(x_s))
        #print("Y range: %s" %(y_s))

        [x_min_str, x_max_str] = re.split("\\.\\.", x_s)
        [y_min_str, y_max_str] = re.split("\\.\\.", y_s)
        x_min = int(x_min_str)
        x_max = int(x_max_str)
        y_min = int(y_min_str)
        y_max = int(y_max_str)

        corners = {
                "x_min": x_min,
                "x_max": x_max,
                "y_min": y_min,
                "y_max": y_max,
                }

        #print("X range: %d -> %d"%(x_min, x_max))
        #print("Y range: %d -> %d"%(y_min, y_max))

        y_point = (y_min * ( y_min+1))/2
        #print( "Part 1: The max y is: %d" % (y_point))

        hits = shoot_points(corners)
        print("Wrong answer for full version: 5884, 6384")
        print("Part 2 hits: %d" %(hits))



if __name__ == "__main__":
    main()
