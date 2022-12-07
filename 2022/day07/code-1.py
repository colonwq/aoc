#!/usr/bin/python3
'''
Solution for Day00 part 1
This is a generic file for all days.
Copy this directory to the new day and part
'''

import sys

def process_input(lines):
    '''This process the command input and output
    and return the dir struct.'''
    dir_struct = { "/": 0 }
    cur_path = []

    for line in lines:
        #print("line: %s"% (line) )
        if line.startswith("$ cd"):
            sub_dir = line[line.rindex(" "):]
            sub_dir = sub_dir.lstrip( " ")
            #print("chdir: %s" % (sub_dir) )
            if sub_dir == "..":
                #print("Pop")
                cur_path.pop()
                #print(cur_path)
            elif sub_dir == "/":
                #print("Pop top")
                cur_path.clear()
                cur_path.append("/")
                #print(cur_path)
            else:
                #print("Push")
                cur_path.append(sub_dir)
                #print(cur_path)
                #full_path = "/".join(cur_path)
                #full_path_parts = full_path.split()
                #full_path = "".join(full_path_parts[1:])
                #print("Full path: %s" %(full_path))
        elif line.startswith("$ ls"):
            #yeah I am not doing anything
            #
            pass
        elif line.startswith("dir"):
            sub_dir = line[line.rindex(" "):]
            sub_dir = sub_dir.lstrip( " ")
            #print("Sub directory: %s"%(sub_dir))
            curr_dir = "/".join(cur_path)
            curr_dir += "/" + sub_dir
            #print("Sub directory: %s"%(curr_dir))
            if not ( curr_dir in dir_struct):
                #print("Adding curr_dir to dir_struct: %s"%(curr_dir))
                dir_struct[curr_dir] = 0
            else:
                print("Already saw directory: %s" %(full_path))
        if line[0].isdigit():
            full_path = "/".join(cur_path)
            #file_size = int(line[line.index(" "):])
            file_size = int(line[:line.index(" ")])
            #print("file size: %s" % (file_size))
            #print("Adding %s to %s" % (file_size, full_path))
            dir_struct[full_path] += file_size

    return dir_struct

def find_dirs(dir_struct):
    '''This will find all the directories
    with more than 100000  size'''
    answer = 0
    max_size = 100000

    poss_dirs = []

    sub_dirs = dir_struct.keys()
    for sub_dir in sub_dirs:
        #print("Looking at subdir: %s -> %d"%(sub_dir, dir_struct[sub_dir]))
        if dir_struct[sub_dir] <= max_size:
            my_size = 0
            #print("Match dir: %s"%( sub_dir))
            my_size += dir_struct[sub_dir]
            for test_dir in sub_dirs:
                if test_dir.startswith(sub_dir) and not(test_dir == sub_dir):
                    #print("Add this dir: %s"%(test_dir))
                    my_size += dir_struct[test_dir]
            if my_size <= max_size:
                print("%s -> %d"%(sub_dir,my_size))
                answer += my_size

    return answer

def find_delete_dir(dir_struct):
    '''this will find the total size of the files
    determine the amount free
    determine the amount need to delete
    find a directory to delete
    '''

    drive_size = 70000000
    min_free =   30000000
    total_size = 0
    unused_size = 0
    min_delete = 0
    answer = 0
    sub_dirs = dir_struct.keys()
    poss_dirs = list()
    for sub_dir in sub_dirs:
        #print("%s -> %d" %(sub_dir, dir_struct[sub_dir]))
        total_size += dir_struct[sub_dir]

    print("Total used: %d" % (total_size))
    unused_size = drive_size - total_size
    print("Unused size: %d" % ( unused_size) )
    min_delete = min_free - unused_size
    print("Need to delete: %d"%(min_delete))

    for sub_dir in sub_dirs:
        #if dir_struct[sub_dir] >= min_delete:
            my_size = 0
            #print("Match dir: %s"%( sub_dir))
            my_size += dir_struct[sub_dir]
            for test_dir in sub_dirs:
                if test_dir.startswith(sub_dir) and not(test_dir == sub_dir):
                    #print("Add this dir: %s"%(test_dir))
                    my_size += dir_struct[test_dir]
            if my_size >= min_delete:
                #print("%s -> %d"%(sub_dir,my_size))
                if answer == 0:
                    answer += my_size
                else:
                    answer = min(answer, my_size)

    return answer

def main():
    """Script entry point"""
    print("Hello World")
    answer = 0
    input_lines = list()
    dir_struct = dict()
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
        input_lines.append(line)

    dir_struct = process_input(input_lines)
    #print(dir_struct)
    answer = find_delete_dir(dir_struct)

    print("Answer %d" % (answer) )

if __name__ == "__main__":
    main()
