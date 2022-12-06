#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def check_window(window):
    '''return true if all leters are unique'''

    window_check = []
    i = 0
    while i < 3:
        test_window = list(window)
        test_char = test_window.pop(i)
        #print("Looking for %s in %s"%(test_char,test_window))
        try:
            test_window.index(test_char)
        except ValueError as v_e:
            #print("%s not in window"%( test_char))
            window_check.append(True)
        else:
            #print("%s IN window"%( test_char))
            window_check.append(False)
        i += 1
        
    #full_window = window_check[0] and window_check[1] and window_check[2]
    #print("Full Window check  : " , full_window)
    full_check_2 = True
    #i = 0
    for check in window_check:
        full_check_2 = full_check_2 and check
    #print("Full Window check 2: ", full_check_2)
    return full_check_2

def check_line(line):
    '''this function will check the give line 
    and return the first location where the next 7
    chars are unique. I guess we assume it is before
    the end of the line'''

    start_pos = 0
    answer = 0
    while start_pos < len(line)-3:
        window = line[start_pos:start_pos+4]
        #print("Window: ", window)
        if check_window(window):
            return start_pos+4
        start_pos += 1
    
    return answer

def main():
    """Script entry point"""
    print("Hello World")
    answer = 0
    #file_input = open(sys.argv[1], "r")

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

        answer = check_line(line)
        print("Answer %d" % (answer) )


if __name__ == "__main__":
    main()
