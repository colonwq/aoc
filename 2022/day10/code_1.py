#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def run_code(code):
    '''this funciton will run the code and do something
    I need the X register
    probably eip
    probably tick '''
    answer = 0
    reg_X = 1
    eip = 0
    #tick = [1]
    tick = []

    for instruction in code:
        #print("Instructoin: %s"%(instruction))
        eip += 1
        if instruction == "noop":
            tick.append(reg_X)
            #print("Ins: %08s Tick: %d X %d" %(instruction,len(tick), reg_X))
        else:
            oper, arg = instruction.split(" ")
            arg = int(arg)
            #print("Oper: %s arg: %s" %( oper, arg))
            tick.append(reg_X)
            #print("Ins: %08s Tick: %d X %d" %(instruction,len(tick), reg_X))
            tick.append(reg_X)
            reg_X += arg
            #print("Ins: %08s Tick: %d X %d" %(instruction,len(tick), reg_X))

    #print("Tick len: %d reg_X: %d" %( len(tick), reg_X))

    return tick

def main():
    """Script entry point"""
    #print("Hello World")
    answer = 0
    lines = []

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
        lines.append(line)

    ticks = run_code(lines)
    output = str()
    i = 0
    while i < len(ticks):
        if(i%40 == 0):
            #print("")
            output += "\n"
        sprite = i%40
        #print("sprite: %02d X %02d" %(sprite, ticks[i]))
        if sprite>= ticks[i]-1 and sprite<=ticks[i]+1:
            #print("x",end="")
            output+="#"
        else:
            #print(".",end="")
            output+=" "
        i+=1


    print(output)

    #print("Answer %d" % (answer) )
    #print("Answer \n" , str(output))

if __name__ == "__main__":
    main()
