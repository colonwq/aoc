#!/usr/bin/python3
'''
Day 16 part 1... some kind of protocol decoder
'''

import re

def main():
    '''
    Here is where dragons occur
    '''
    in_file = open("../day17.data")
    #in_file = open("../day17.demo")

    for line in in_file:
        line = line.rstrip("\r\n")
        print("Line: %s" % (line))

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

        print("X range: %d -> %d"%(x_min, x_max))
        print("Y range: %d -> %d"%(y_min, y_max))

        y_point = (y_min * ( y_min+1))/2
        print( "The max y is: %d" % (y_point))



if __name__ == "__main__":
    main()
